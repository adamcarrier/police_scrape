# Newport News Police Incident Scraper

This project allows you to gather and save all the following reports from the City of Newport News Police Department:

*Daily Offense Reports:*

* [Sunday](https://www2.nngov.com/newport-news/offenses/suntxt.htm)
* [Monday](https://www2.nngov.com/newport-news/offenses/montxt.htm)
* [Tuesday](https://www2.nngov.com/newport-news/offenses/tuetxt.htm)
* [Wednesday](https://www2.nngov.com/newport-news/offenses/wedtxt.htm)
* [Thursday](https://www2.nngov.com/newport-news/offenses/thutxt.htm)
* [Friday](https://www2.nngov.com/newport-news/offenses/fritxt.htm)
* [Saturday](https://www2.nngov.com/newport-news/offenses/sattxt.htm)

*Daily Arrest Reports:*

* [Sunday](https://www2.nngov.com/newport-news/arrests/suntxt.htm)
* [Monday](https://www2.nngov.com/newport-news/arrests/montxt.htm)
* [Tuesday](https://www2.nngov.com/newport-news/arrests/tuetxt.htm)
* [Wednesday](https://www2.nngov.com/newport-news/arrests/wedtxt.htm)
* [Thursday](https://www2.nngov.com/newport-news/arrests/thutxt.htm)
* [Friday](https://www2.nngov.com/newport-news/arrests/fritxt.htm)
* [Saturday](https://www2.nngov.com/newport-news/arrests/sattxt.htm)

To configure the project to write to your Firebase database:

 1. Download your Firebase JSON service account key, and put it into the same folder as this project.
 2. Rename the `firebase_config_sample.py` file to `firebase_config.py`.
 3. In the `firebase_config.py` file, change the `'serviceAccountKey.json'` filename to match your service key's filename.
 4. Change the `firebase_database_url` to your Firebase database's URL.

 To configure the project to automatically geocode the addresses (i.e., get the formatted address, latitude, and longitude):
 1. Rename the `gcp_config_sample.py` file to `gcp_config.py`.
 2. In the `gcp_config.py` file, change the `gcp_api_key` API key to your Google Cloud Platform API key.

## Running the script
Before running the script, you'll need to install the following as root. This is an example for CentOS:
```
% yum install python3 python3-devel gcc-c++
% pip3 install BeautifulSoup4
% pip3 install firebase_admin
```

To run the script:
```
% python3 police_scrape.py
```
Optionally, you can run the script only for today's reports. This is useful when automating this to run one or more times a day. There's no need to re-pull and re-process reports from previous days, especially considering geocoding is done for each incident, which uses metered Google Cloud resources.
```
% python3 police_scrape.py today
```
