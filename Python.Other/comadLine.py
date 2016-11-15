import sys
from lxml.html import parse,tostring,open_in_browser,fromstring
from urllib.request import urlopen

if __name__ == '__main__':
    if len(sys.argv) > 1 :
        url = str().join(sys.argv[1:])
        respons = urlopen(url)
    html = b''
    for lineTag in respons.readlines():
        buff = b''
        if b'style=' in lineTag:
            startTag = lineTag.find(b'style=')
            endTag = lineTag.find(b'>')
            buff += lineTag[:startTag]
            buff += lineTag[endTag:]
        else:
            buff = lineTag
        html += buff
    htmlDoc = fromstring(html)
    open_in_browser(htmlDoc)

