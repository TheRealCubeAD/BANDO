import urllib.request
import json
import csv
import sqlite3

base_url = "https://hacker-news.firebaseio.com/v0/"

class HackerStore:
    def __init__(self, n_id):
        self.own_id = n_id
        self.url = self.get_url()
        print(self.url)
        self.data = None

        self.load_item()
        print(self.data)


    def load_item(self):   #requests json from given url and loads it into dictionary
        response = urllib.request.urlopen(self.url)
        try:
            self.data = json.loads(response.read())
        except json.decoder.JSONDecodeError:
            self.data = None


    def get_url(self):  #converts id to url
        return base_url + "item/" + str(self.own_id) + ".json"


    def is_data(self):
        return bool(self.data)


    def store(self, path):
        pass


class HackerStoreCSV(HackerStore):
    def store(self, path):  #stores into csv file !work in progress!
        file = open(path, 'w')
        output = csv.writer(file)
        output.writerow(self.data.keys())
        output.writerow(self.data.values())


class HackerStoreSqlite(HackerStore):
    def store(self, path):  #stores into sql file !work in progress!
        table_name = "HS" + str(self.own_id)
        conn = sqlite3.connect(path)
        c = conn.cursor()
        c.execute("CREATE TABLE " + table_name + " (None None")
        c.execute("insert into " + table_name + "values (?, ?", [self.own_id, self.data])
        conn.commit()
        conn.close()



def read_max_item():
    data = json.loads(urllib.request.urlopen(base_url + "maxitem.json").read())
    return data


def load_all_stories(mode="CSV"):
    if mode == "CSV":
        sub_class = HackerStoreCSV
    elif mode == "sqlite":
        sub_class = HackerStoreSqlite
    else:
        return
    all_items = []
    maxitem = read_max_item()
    for i in range(maxitem + 1):
        obj = sub_class(maxitem - i)
        if obj.is_data():
            all_items.append(obj)
    return all_items


def load_single_storie(id, mode="CSV"):
    if mode == "CSV":
        sub_class = HackerStoreCSV
    elif mode == "sqlite":
        sub_class = HackerStoreSqlite
    else:
        return
    return sub_class(id)
