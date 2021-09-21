# This program loads documents from urls passed through the command line. It fetches links from the HTMl documents
# prints the number of external urls referenced in the documents. This program does not parse document types other
# than HTML documents.

from bs4 import BeautifulSoup
import sys
import requests
from requests.exceptions import MissingSchema, ConnectionError


def is_external_link(url, base_uri):
    return not (url.startswith(base_uri) or url.startswith('/') or
                url.startswith('./') or url.startswith('../') or url.startswith('#'))


def parse():
    for i in input_args[1:]:
        # Specifies request header
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        }

        try:
            page = requests.get(i, headers=headers)
        except MissingSchema as error:
            print(error)
            sys.exit(1)
        except ConnectionError as error:
            print(error)
            sys.exit(1)

        # Gets the html document for each url
        soup = BeautifulSoup(page.text, 'html.parser')

        external_links = set()

        get_external_links(external_links, i, soup)

        print(i + " " + str(len(external_links)))


def get_external_links(external_links, i, soup):
    # Finds all tags with the href attribute
    href_tags = soup.find_all(href=True)
    hrefs = [tag.get('href') for tag in href_tags]

    # Check each link to see if it's external and if it is add it to the set
    for href in hrefs:
        if is_external_link(href, i):
            external_links.add(href)

    # Finds all tags with the src attribute
    src_tags = soup.find_all(src=True)
    srcs = [tag.get('src') for tag in src_tags]

    # Check each media link to see if it's external and if it is add it to the set
    for src in srcs:
        if is_external_link(src, i):
            external_links.add(src)


if __name__ == '__main__':
    input_args = sys.argv

    if len(input_args) < 2:
        sys.exit('No URLs entered')
    else:
        parse()
