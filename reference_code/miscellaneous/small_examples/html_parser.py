from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
        if attrs:
            print('attributes:', attrs)

    def handle_endtag(self, tag):
        print("Encountered an end tag:", tag)

    def handle_data(self, data):
        if data.strip():
            print("Encountered some data:", data)

    def handle_startendtag(self, tag, attrs):
        print("Found an empty tag:", tag)
        if attrs:
            print('attributes:', attrs)
            
    def handle_comment(self, data):
        if data.strip():
            print("Encountered comment:", data)


sample_html = '''
<html>
    <head>
        <title>Test</title>
    </head>
    <body>
        <h1 name="asd">Parse me!</h1><br/>
        <!--
        <h1 name="NO">NOOOOOO</h1>
        <br/>
        -->
    </body>
</html>
'''

parser = MyHTMLParser()
parser.feed(sample_html)
