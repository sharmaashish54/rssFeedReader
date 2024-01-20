import feedparser
import sys

print(sys.argv)

feed_urls = ""
if len(sys.argv)>1:
    feed_urls = sys.argv[1:]
else:
    print("no url given to show feed")


def final_results():
    

    for url in feed_urls:
        print(f"\n\nShowing Data for url -> {url}\n.............................\n")
        feed = feedparser.parse(url) # https://feeds.bbci.co.uk/news/rss.xml
        if feed['bozo']:
            print("failed to fetch results")
        for entry in feed['entries']:
            print(f'Title: {entry.title}')
            print(f'Description: {entry.description}')
            print(f'Link: {entry.link}\n')
        print("...................................\n\n")


final_results()