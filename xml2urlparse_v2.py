from bs4 import BeautifulSoup
import urllib.request
import lxml
import pandas as pd
#import logging

urlstart = 'https://www.domain.com/sitemap_index.xml'

# Function to parse XML for urls
def xmlparse(urlstart):
    urllist = []
    ## Parse and Cleanup the XML
    req = urllib.request.urlopen(urlstart)
    xml = BeautifulSoup(req, 'lxml')
    for item in xml.findAll('loc'):
        urllist.append(str(item))
    for x in range(len(urllist)):
        urllist[x] = urllist[x].replace("<loc>", "")
        urllist[x] = urllist[x].replace("</loc>", "")

    ## Grab the urls; and build the big final list of urls and suburls
    url_interm = []
    for url in urllist:
        if url.endswith(".xml"):
            url_interm.append(url)
            # recursively call the function; if we have a .xml subdomain
            # this lets us grab the nested levels of xml pages
            burner_list = xmlparse(url)
            # url_interm list combination of the suburls to our base url
            url_interm = url_interm + burner_list
        else:
            # If the url doesnt have .xml at the end, append it, and keep going
            url_interm.append(url)
    # our final output to the user
    return url_interm


output = xmlparse(urlstart)

# Get the data into a dataframe
df = pd.DataFrame(output, columns=['url'])

# Then export to a csv
df.to_csv('urls.csv')

# Tell me it worked!
print("The output csv file written successfully and generated...")

