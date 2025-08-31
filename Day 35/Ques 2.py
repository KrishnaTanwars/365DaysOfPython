# Question: Given N lines of HTML code, parse it to print the tags, attributes, and attribute values.


from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print(f"-> {attr} > {value}")

n = int(input())
html_input = "\n".join(input() for _ in range(n))
parser = MyHTMLParser()