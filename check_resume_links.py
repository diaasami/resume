from html.parser import HTMLParser
import sys
import requests


class GetLinksParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            d_attrs = dict(attrs)
            if 'href' in d_attrs and d_attrs['href'].startswith('http'):
                self.links.append(d_attrs['href'])


class IsCustomized404Page(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.is_custom_404_page = False

    def handle_data(self, data):
        if self.is_custom_404_page:
            return

        if '404' in data.split():
            self.is_custom_404_page = True
        elif data.find('Not Found') > -1:
            self.is_custom_404_page = True


if __name__ == "__main__":
    parser = GetLinksParser()
    parser.feed(open(sys.argv[1]).read())
    links = parser.links
    parser.close()

    failed = 0

    for link in links:
        try:
            # print(f"GETting {link}")
            r = requests.get(link)
            if 'Content-Type' in r.headers and r.headers['Content-Type'].startswith('text/html'):
                parser = IsCustomized404Page()
                parser.feed(r.text)
                parser.close()
                probable_404_page = parser.is_custom_404_page
                if probable_404_page:
                    print(f"Link {link} is probably customized 404 page")
                    failed += 1

        except requests.RequestException as e:
            print(f"Error {e} getting {link}")
            failed += 1

    sys.exit(1 if failed else 0)
