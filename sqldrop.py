#!/usr/bin/env python
#coding:utf-8

import requests
import urlparse
import re
import os, sys
import optparse

def httpGetMethod(URL, params):
    try:
        print "\n[+] Testing Connection "
        request = requests.get(URL, params)
        print "[+] HTTP Response: " + str(request.status_code) +  " " + request.reason
    except Exception, e:
        print "[-] HTTP Connection Error :" + str(e)
        exit(0)

def main():

    parser = optparse.OptionParser('usage: %prog ' + 'fuck SQL injection')
    parser.add_option('-u', dest = 'URL', type = 'string', help = 'Target URL (e.g. "http://www.example.com/vul.php?id=1")')
    parser.add_option('-d', dest = 'databases', type = 'string', help = '')
    parser.add_option('-t', dest = 'tables', type = 'string', help = '')
    parser.add_option('-c', dest = 'columns', type = 'string', help = '')
    parser.add_option('--dump', dest= 'true', type = 'string', help = '')
    (options, argvs) = parser.parse_args()

    if options:
        requestURL = urlparse.urlparse(options.URL)
        httpGetMethod(requestURL.scheme + "://" + requestURL.hostname + requestURL.path, requestURL.query)
    else:
        exit(0)

if __name__ == '__main__':
    main()