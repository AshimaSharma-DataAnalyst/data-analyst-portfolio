from bs4 import BeautifulSoup


class HTMLParser:

    def parse_html(self, html):

        return BeautifulSoup(html, "html.parser")


    def get_title(self, soup):

        if soup.title:
            return soup.title.text.strip()

        return ""


    def get_h1(self, soup):

        h1 = soup.find("h1")

        if h1:
            return h1.text.strip()

        return ""


    def get_all_paragraphs(self, soup):

        paragraphs = []

        for p in soup.find_all("p"):

            text = p.get_text(" ", strip=True)

            if text:

                paragraphs.append(text)

        return paragraphs


    def get_meta_description(self, soup):

        meta = soup.find("meta", attrs={"name": "description"})

        if meta:

            return meta.get("content", "")

        return ""


    def get_all_links(self, soup):

        links = []

        for link in soup.find_all("a", href=True):

            links.append({

                "text": link.get_text(strip=True),

                "url": link["href"]

            })

        return links


    def get_all_images(self, soup):

        images = []

        for image in soup.find_all("img"):

            images.append({

                "src": image.get("src"),

                "alt": image.get("alt")

            })

        return images


    def get_all_tables(self, soup):

        tables = []

        for table in soup.find_all("table"):

            tables.append(str(table))

        return tables


    def get_infobox(self, soup):

        info = {}

        table = soup.find("table", class_="infobox")

        if table is None:

            return info

        rows = table.find_all("tr")

        for row in rows:

            th = row.find("th")

            td = row.find("td")

            if th and td:

                key = th.get_text(" ", strip=True)

                value = td.get_text(" ", strip=True)

                info[key] = value

        return info
