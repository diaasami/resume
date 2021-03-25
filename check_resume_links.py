from html.parser import HTMLParser
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

if __name__ == "__main__":
    parser = GetLinksParser()
    parser.feed(open("./Downloads/diaasami_resume.html").read())
    links = parser.links
    
    #[print(l) for l in parser.links]

    for link in links:
        print(f"GETting {link}")
        try:
            r = requests.get(link)
            if 'content-type' in r.headers and headers['content-type'].startswith('text/html'):
                parser = IsCustomized404Page()
                parser.feed(r.text)
                probable_404_page = parser.is_custom_404_page
                if probable_404_page:
                    print("Link is probably customized 404 page")
            
        except requests.RequestException as e:
            print(e)




