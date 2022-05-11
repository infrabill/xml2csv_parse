# xml2csv_parse
This will take a site xml, and parse out a list of the urls within. This will also process multiple levels of the xml.

Once run, you will get a message stating it worked, and with in the directory of the script will be a url.csv with the output.


## Built With
- bs4
- urllib.request
- lxml
- pandas

## Getting Started
To set up this project locally, follow these steps.

## Prerequisites
- beautifulsoup4         4.11.1
- lxml                   4.8.0
- pandas                 1.3.5
- urllib3                1.26.7

## Installation
1. Clone the repo
2. Install package dependencies using PIP

```
pip3 install requirements.txt
```

3. Enter in url for xml you want to parse, within the script.
```
urlstart = 'https://www.domain.com/sitemap_index.xml'
```


4. Run
```
python3 xml2urlparse.py
```

