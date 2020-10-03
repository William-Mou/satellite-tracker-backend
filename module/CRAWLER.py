import NASASQL
import requests
import json

import csv


#text = '{"info":{"satname":"SPACE STATION","satid":25544,"transactionscount":1},"positions":[{"satlatitude":-18.24982199,"satlongitude":6.36988326,"sataltitude":425.45,"azimuth":108.39,"elevation":-46.6,"ra":196.76667706,"dec":-40.11030795,"timestamp":1601716594,"eclipsed":false},{"satlatitude":-18.20071261,"satlongitude":6.4099987,"sataltitude":425.44,"azimuth":108.33,"elevation":-46.59,"ra":196.78903678,"dec":-40.06976541,"timestamp":1601716595,"eclipsed":false},{"satlatitude":-18.15159263,"satlongitude":6.45008953,"sataltitude":425.42,"azimuth":108.27,"elevation":-46.59,"ra":196.81141043,"dec":-40.02922804,"timestamp":1601716596,"eclipsed":false},{"satlatitude":-18.1024601,"satlongitude":6.49015744,"sataltitude":425.4,"azimuth":108.2,"elevation":-46.59,"ra":196.83379892,"dec":-39.9886942,"timestamp":1601716597,"eclipsed":false},{"satlatitude":-18.05332099,"satlongitude":6.53019768,"sataltitude":425.39,"azimuth":108.14,"elevation":-46.59,"ra":196.85619954,"dec":-39.94816881,"timestamp":1601716598,"eclipsed":false},{"satlatitude":-18.00416742,"satlongitude":6.57021677,"sataltitude":425.37,"azimuth":108.08,"elevation":-46.58,"ra":196.8786159,"dec":-39.90764535,"timestamp":1601716599,"eclipsed":false},{"satlatitude":-17.95500536,"satlongitude":6.61020996,"sataltitude":425.36,"azimuth":108.02,"elevation":-46.58,"ra":196.90104529,"dec":-39.86712871,"timestamp":1601716600,"eclipsed":false},{"satlatitude":-17.90583288,"satlongitude":6.65017893,"sataltitude":425.34,"azimuth":107.95,"elevation":-46.58,"ra":196.92348861,"dec":-39.82661728,"timestamp":1601716601,"eclipsed":false},{"satlatitude":-17.85665,"satlongitude":6.69012377,"sataltitude":425.32,"azimuth":107.89,"elevation":-46.58,"ra":196.94594588,"dec":-39.78611106,"timestamp":1601716602,"eclipsed":false},{"satlatitude":-17.80745676,"satlongitude":6.73004456,"sataltitude":425.31,"azimuth":107.83,"elevation":-46.57,"ra":196.96841707,"dec":-39.74561005,"timestamp":1601716603,"eclipsed":false}]}'

class CRAWLER:
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
