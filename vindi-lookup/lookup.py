import feedparser
import json
from datetime import datetime
from os import path

RESULTS_DESTINATION = '.'

def categorize_entry(text: str):
    categories = [
        ("geweld", ["geweld", "vechtpartij", "gevecht", "mishandeling"]),
        ("asociaal", ["gooien", "lastig vallen", "schreeuwen", "overlast"]),
        ("dierenmishandeling", ["dier", "dieren"])
    ]

    for category, matches in categories:
        if any(match in text for match in matches):
            return category
    return "geen-categorie"

def check_existing_entries(entry: str, destination: str):
    file_name = "result"
    full_path = destination + "/" + file_name + ".json"
    if path.isfile(full_path) is False:
      raise Exception(full_path + " niet gevonden")

    exists = False

    try:
        with open(full_path, 'r') as fp:
            json_object = json.load(fp)
            for item in json_object:
                if entry == item["title"]:
                    print(entry + " bestaat al")
                    exists = True
                    break
    except json.decoder.JSONDecodeError:            
        print("Bestand is leeg dus valt niet te parsen als json_object.")

    return exists

def search_rss_feed(rss_urls: list):
    results = []
    for url in rss_urls:
        print(url)
        feed = feedparser.parse(url)
        for entry in feed.entries:
            if "een" in entry.title or "vindicat" in entry.description:
                category = categorize_entry(str(entry.title) + " " + str(entry.description))
  
                result = { 
                    "title": entry.title,
                    "link": entry.link,
                    "date": "derp",
                    "category": category
                }

                if check_existing_entries(entry.title, RESULTS_DESTINATION) is False:
                    print("artikel bestaat nog niet dus toevoegen")
                    results.append(result)
                    dump_results_as_json(results, RESULTS_DESTINATION)

    return results

def dump_results_as_json(result: dict, destination: str):
    file_name = "result"
    full_path = destination + "/" + file_name + ".json"
    if path.isfile(full_path) is False:
      raise Exception(full_path + " niet gevonden")
    
    with open(full_path, 'w') as fp:
        json.dump(result, fp)

def collect_news_items():
    rss_urls = ['https://ukrant.nl/rss']
    # rss_urls = ['https://ukrant.nl/rss',
    #             'https://rtvnoord.nl/rss/',
    #             'https://www.gic.nl/startpagina/rss',
    #             'https://www.sikkom.nl/api/feed/rss',
    #             'https://feeds.nos.nl/nosnieuwsalgemeen',
    #             'https://www.oogtv.nl/rss']

    results = search_rss_feed(rss_urls)
    # print(results)
