#!/usr/bin/python
import sys
import requests
import json

print'''
       \033[3;37;37m [+]Back to the history by Hannan Haseeb... \033[3;31;31m
'''
def waybackurls(host, with_subs):
    if with_subs:
        url = 'http://web.archive.org/cdx/search/cdx?url=*.%s/*&output=html&fl=original&collapse=urlkey' % host
    else:
        url = 'http://web.archive.org/cdx/search/cdx?url=*.%s/*&output=html&fl=original&collapse=urlkey' % host
    r = requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"})
    #results = r.json()
    return r.text #[1:]


if __name__ == '__main__':
    argc = len(sys.argv)
    if argc < 2:
        print('Usage:\n\tpython timescript.py <url> <include_subdomains:optional>')
        sys.exit()

    host = sys.argv[1]
    with_subs = False
    if argc > 3:
        with_subs = True

    urls = waybackurls(host, with_subs)
    #json_urls = json.dumps(urls)
    #if urls:
        #pure_url = json.loads(json_urls)
        #for thelink in pure_url:
        #       print thelink[0]
    #for i in urls:
    print urls
    filename = '%s-history.json' % host
    with open(filename, 'w') as f:
           f.write(urls)
    print('\033[3;37;37m[*] Saved result to %s' % filename)
