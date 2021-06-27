#!/usr/bin/env python3
# Main script for running the police data collection and firebase sync modules

import sys, requests, json, re, datetime
import nnpd_pages
from bs4 import BeautifulSoup
from firebase_sync import save_offense, save_arrest, init_db

def main():
    day = ''
    scope = 'all'
    if len(sys.argv) > 1 and sys.argv[1] == 'today':
        scope = 'today'
        today = datetime.date.today()
        day = today.strftime("%A")  # Ex: "Sunday"

    # Init the Firebase DB (only do this once)
    init_db()

    # Scrape the Daily Offense Reports
    pages = nnpd_pages.get_offense_pages()
    today = {}

    # If desired, get only today's page
    if scope == 'today':
        for item in pages.items():
            if item[0] == day:
                today[item[0]] = item[1]
        pages = today

    for page in pages:
        html = requests.get(pages[page])
        soup = BeautifulSoup(html.content, 'html.parser')

        # Get column headings
        columns = []
        header = soup.find('thead')
        headings = header.findAll('th')
        for heading in headings:
            columns.append(capitalize_words(heading.text))

        # Get report rows
        rows = soup.findAll('tr')
        for row in rows:
            fields = row.findAll("td")
            if fields is not None and len(fields) > 0:
                report = {}
                n = 0
                for field in fields:
                    while n < len(columns):
                        text = ' '.join(fields[n].get_text().split())
                        report[columns[n]] = text
                        n = n + 1
                # print(json.dumps(report))
                save_offense('nnpd', 'NEWPORT NEWS, VA', json.dumps(report))

    # Scrape the Daily Arrest Reports
    pages = nnpd_pages.get_arrest_pages()
    today = {}

    # If desired, get only today's page
    if scope == 'today':
        for item in pages.items():
            if item[0] == day:
                today[item[0]] = item[1]
        pages = today

    for page in pages:
        html = requests.get(pages[page])
        soup = BeautifulSoup(html.content, 'html.parser')

        # Get page date
        dateline = soup.find('center', text=re.compile('Last Update'))
        mmddyyyy = re.findall(r"(\d+)(\/\d+)(\/\d+)", str(dateline))
        date =  ' '.join(''.join(xx) for xx in mmddyyyy)

        # Get first row, which has the column headings
        columns = []
        columns.append('Date')

        header = soup.find('tr')
        headings = header.findAll('td')
        for heading in headings:
            columns.append(capitalize_words(heading.text))

        # Get report rows (all rows after the first)
        rows = soup.findAll('tr')[1:]
        for row in rows:
            fields = row.findAll("td")
            if fields is not None and len(fields) > 0:
                report = {}
                n = 0
                for field in fields:
                    while n < (len(columns)-1):
                        text = ''
                        if (n == 0):
                            text = date
                            report[columns[n]] = text
                        text = ' '.join(fields[n].get_text().split())
                        report[columns[n+1]] = text
                        n = n + 1
                # print(json.dumps(report))
                save_arrest('nnpd', 'NEWPORT NEWS, VA', json.dumps(report))

def capitalize_words(s):
    words = re.findall(r'\w+', s)
    return ''.join(map(str.title, words[0:]))

if __name__ == "__main__":
    main()