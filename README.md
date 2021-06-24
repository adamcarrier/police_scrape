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

 To run the script:
 ```
 % python3 police_scrape.py
 ```