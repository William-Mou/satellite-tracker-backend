from module import NASASQL
import requests
import json
import csv
import satalist.csv

class newcraw:
    """
    docstring
    """
    def __init__(self):
        self.time_range = 10

        with open('satalist.csv', newline='') as f:
            reader = csv.reader(f)
            id_ist = list(reader)[0]

        print(id_ist)
        self.id_list = id_ist

    def update(self) :
        for i in self.id_list:
            r = requests.get("https://www.n2yo.com/rest/v1/satellite/positions/"+str(i)+"/41.702/-76.014/0/"+ str(self.time_range) +"/&apiKey=CANKX6-M9DBXS-Y9ZHSL-4KCJ")
            text = r.text
            print(i)
            nasadict = json.loads(text)
            print(nasadict)
            satname = nasadict["info"]["satname"]
            for time_i in range(self.time_range):
                timestamp = nasadict["positions"][time_i]["timestamp"]
                satlatitude = nasadict["positions"][time_i]["satlatitude"]
                satlongitude = nasadict["positions"][time_i]["satlongitude"]
                sataltitude = nasadict["positions"][time_i]["sataltitude"]

                SQL = NASASQL.NASASQL(i)
                SQL.connect_SQL()
                SQL.insert_SQL(timestamp,satname,satlatitude,satlongitude,sataltitude)
            




def getName(id):
    print(nasadict["info"][satname])
    return nasadict["info"][satname]
