# html-document-parser-python

CONTENTS OF THIS FILE
=====================

* Introduction
* Requirements
* Installation

INTRODUCTION
============

Given a list of HTTP and HTTPS URLs as arguments, this program retrieves each URL as a document and returns the number of unique external URLs referenced in the document.
The program parses HTML document responses. For example, an invocation with a list of URLs should look something like "python main.py http://example.com http://www.columbia.edu/~fdc/sample.html".
For each valid URL, the program prints a line consisting of the URL and the number of external links in the retrieved document, separated by a space, like "http://example.com 1".
Each URL is printed on its own line of the output.

REQUIREMENTS
============

* This program needs python 2.7 and above

INSTALLATION
============

* Type sudo easy_install . to install the project
* If easy_install does not work:
    * For python 3+: type sudo python3 setup.py install
    * For python 2.7: type sudo python setup.py install

HOW TO RUN THE PROGRAM
======================
* Type cd src/html_parser_package
* Type python main.py url1 url2 url3 etc
* For example: python main.py https://google.com
