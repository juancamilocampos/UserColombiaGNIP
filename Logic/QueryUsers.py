from Config.config import Configuration
from pymongo import MongoClient
from unidecode import unidecode
import csv
import os


class QueryUsers:

    def __init__(self):
        self.ConfigApi = Configuration()
        self.client = MongoClient()
        self.db = self.client[self.ConfigApi.MONGO_DB()]
        self.unitext = lambda text: unidecode(text).lower()
        self.country = self.unitext("Colombia")
        self.departments = list()

        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        rel_path = "l_location.csv"
        file_path = os.path.join(script_dir, rel_path)

        file = open(file_path, encoding='latin_1')
        aux_list = csv.reader(file, delimiter=';')
        for row in aux_list:
            self.departments.append(self.unitext(row[9]))

        self.departments = [x for x in self.departments if x != ""]
        self.departments = list(self.departments)
        self.cities = ["leticia", "medellin", "arauca", "barranquilla", "cartagena", "tunja", "manizales",
                       "florencia", "yopal", "popayan", "valledupar", "quibdo", "monteria", "bogota",
                       "puerto Inirida", "san jose del guaviare", "neiva", "rioacha", "santa marta",
                       "villavicencio", "pasto", "cucuta", "mocoa", "armenia", "pereira", "san andres",
                       "bucaramanga", "sincelejo", "ibague", "cali", "mitu", "puerto carreño", "soledad ",
                       "bello ", "soacha", "buenaventura", "palmira", "itagui", "floridablanca", "envigado",
                       "tulua", "tumaco", "dos quebradas"]

        self.places = self.departments + self.cities

    def query_users(self):
        users = list()
        for day in range(24, 28):
            coll = self.db['tweetsGNIP'+str(day)]
            users = users + coll.distinct("actor.id")
        print(len(list(set(users))))

    def _colombianq(self, location):
        location = self.unitext(location)
        if self.country in location:
            return True
        else:
            for city in self.places:
                if city in location:
                    return True

            return location
             #return False

    def test_colombianq(self):

        coll = self.db['tweetsGNIP24']
        cursor = coll.find({'gnip.matching_rules.0.tag': "TagProfileCountryCode"}, {'actor.location': 1})
        bad_places = list()
        for element in cursor:
            col = self._colombianq(element["actor"]["location"]["displayName"])
            if type(col) == str:
                bad_places.append(col)

        bad_places = list(set(bad_places))
        print (bad_places)
        print(len(bad_places))