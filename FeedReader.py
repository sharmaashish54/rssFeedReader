#!/usr/bin/python3

'''This is multiline comment'''

from feedparser import parse, USER_AGENT
from os import system

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0"


def get_url_list():
    rss_url_list = []

    while True:
        url = input("Input a RSS feed URL. Press q to quit: ")
        if url == "q":
            break
        if url == "":
            continue

        rss_url_list.append(url)

    system("clear")
    return rss_url_list


def parse_url(rss_url):

    try:
        response = parse(rss_url)

        print("Feed Details")
        print(f"\t{response.feed.title}")
        print(f"\t{response.feed.description}")
        print(f"\t{response.feed.link}")
        print()

        for item in response.entries:
            print(f"Title: {item.title}")
            print(f"Description: {item.description}")
            print(f"Link: {item.link}")
            print()
    except Exception:
        print(f"{rss_url} is not a valid RSS feed input")
        print()


rss_url_list = get_url_list()

if rss_url_list:
    for rss_url in rss_url_list:
        parse_url(rss_url)