import requests
import xml.etree.ElementTree as ET


def parsed(url):
    print(f"\n\nShowing Data for url -> {url}\n.............................\n")
    r = requests.get(url)

    if r.status_code==200:
        root = ET.fromstring(r.content)

        for elem in root.iter():
            print(f"{elem.tag}: {elem.text}")

    print("...................................\n\n")