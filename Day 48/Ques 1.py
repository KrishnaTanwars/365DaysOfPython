# Question: Parse an HTML string and print the start tags, end tags, and their attributes.

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for name, value in attrs:
            print(f"-> {name} > {value}")
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for name, value in attrs:
            print(f"-> {name} > {value}")

n = int(input())
html = ""
for _ in range(n):
    html += input().strip() + "\n"
parser = MyHTMLParser()
parser.feed(html)
