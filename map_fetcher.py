﻿import requests
import json

from graph_creator import GraphCreator

class MapFetcher:
    """
    mapFetcher uses requests and json to fetch the map details from the internet
    given the building and level. 
    If incorrect building/level is given, #TODO: what to do?
    info, map and wifi are retrieved using getInfo, getMap, getWifi
    Data is returned in raw form.
    """
    URL_STANDARD = "http://ShowMyWay.comp.nus.edu.sg/getMapInfo.php?"

    def __init__(self):
        self._map = ""
        self.info = ""
        self.wifi = ""

        self.building = ""
        self.level = ""

        self.graphcreator = GraphCreator()
        self.maplist = ""
        self.edges = ""

    def fetch_map(self, building, level):
        self.building = str(building)
        self.level = str(level)

        url = MapFetcher.URL_STANDARD + "Building=" + self.building + "&Level=" + self.level
        try: 
            count = 0
            while(self.info == "" and count < 10):
                REQUEST = requests.get(url)
                data = json.loads(REQUEST.text)
                self.info = data['info']
                count += 1
            if count == 10 :
                print "failed to get map details"
            else:
                self._map = data['map']
                self.wifi = data['wifi']
        except:
            print "failed. Using Static Local Copy..."
            data = json.loads('{"info":{"northAt":"315"},"map":[{"nodeId":"1","x":"0","y":"2558","nodeName":"TO LT15","linkTo":"2"},{"nodeId":"2","x":"2152","y":"2558","nodeName":"P2","linkTo":"1, 3, 4"},{"nodeId":"3","x":"2152","y":"731","nodeName":"Linkway","linkTo":"2"},{"nodeId":"4","x":"2883","y":"2558","nodeName":"P4","linkTo":"2, 5, 6, 7"},{"nodeId":"5","x":"2883","y":"1584","nodeName":"P5","linkTo":"4, 8"},{"nodeId":"6","x":"2883","y":"2924","nodeName":"Seminar Room 6","linkTo":"4"},{"nodeId":"7","x":"3776","y":"2558","nodeName":"Lobby ","linkTo":"4, 10"},{"nodeId":"8","x":"3330","y":"1584","nodeName":"P8","linkTo":"5, 9, 10"},{"nodeId":"9","x":"3330","y":"934","nodeName":"Seminar Room 2","linkTo":"8"},{"nodeId":"10","x":"3776","y":"1584","nodeName":"P10","linkTo":"7, 8, 11"},{"nodeId":"11","x":"5603","y":"1584","nodeName":"Student Area","linkTo":"10, 12, 13, 14"},{"nodeId":"12","x":"5603","y":"2924","nodeName":"Seminar Room 1","linkTo":"11"},{"nodeId":"13","x":"5603","y":"731","nodeName":"P13","linkTo":"11"},{"nodeId":"14","x":"7065","y":"1584","nodeName":"P14","linkTo":"11, 15, 16"},{"nodeId":"15","x":"7065","y":"2802","nodeName":"P15","linkTo":"14, 32"},{"nodeId":"16","x":"7065","y":"731","nodeName":"P16","linkTo":"14, 18"},{"nodeId":"17","x":"9014","y":"2802","nodeName":"P17","linkTo":"32, 19, 21"},{"nodeId":"18","x":"8283","y":"731","nodeName":"P18","linkTo":"16, 20, 22"},{"nodeId":"19","x":"9014","y":"2193","nodeName":"Executive Classroom","linkTo":"17"},{"nodeId":"20","x":"8283","y":"1056","nodeName":"Tutorial Room 11","linkTo":"18"},{"nodeId":"21","x":"9460","y":"2802","nodeName":"P21","linkTo":"17, 23, 24"},{"nodeId":"22","x":"9744","y":"731","nodeName":"P22","linkTo":"18, 25, 34"},{"nodeId":"23","x":"9460","y":"3248","nodeName":"Seminar Room 9","linkTo":"21"},{"nodeId":"24","x":"11003","y":"2802","nodeName":"P24","linkTo":"21, 27, 28"},{"nodeId":"25","x":"9744","y":"1056","nodeName":"NUS Hackers Room","linkTo":"22"},{"nodeId":"26","x":"11003","y":"731","nodeName":"P26","linkTo":"34, 28, 29"},{"nodeId":"27","x":"11003","y":"3248","nodeName":"Seminar Room 11","linkTo":"24"},{"nodeId":"28","x":"11003","y":"1259","nodeName":"P28","linkTo":"24, 26, 30"},{"nodeId":"29","x":"11571","y":"731","nodeName":"P29","linkTo":"26, 31"},{"nodeId":"30","x":"12180","y":"731","nodeName":"TO Canteen","linkTo":"28"},{"nodeId":"31","x":"11774","y":"488","nodeName":"TO COM2-2","linkTo":"29"},{"nodeId":"32","x":"7552","y":"2802","nodeName":"P32","linkTo":"15, 17, 33"},{"nodeId":"33","x":"7552","y":"3086","nodeName":"Seminar Room 7","linkTo":"32"},{"nodeId":"34","x":"10272","y":"731","nodeName":"P34","linkTo":"22, 26, 35"},{"nodeId":"35","x":"10272","y":"447","nodeName":"Tutorial Room 5","linkTo":"34"}],"wifi":[{"nodeId":"1","x":"1503","y":"2558","nodeName":"arc-0201-a","macAddr":"e8:ba:70:61:c9:60"},{"nodeId":"2","x":"2599","y":"2924","nodeName":"arc-0202-a","macAddr":"e8:ba:70:61:af:20"},{"nodeId":"3","x":"2964","y":"731","nodeName":"arc-0204-a","macAddr":"04:da:d2:74:cf:30"},{"nodeId":"4","x":"5481","y":"1624","nodeName":"arc-0205-a","macAddr":"e8:ba:70:52:3b:e0"},{"nodeId":"5","x":"4060","y":"609","nodeName":"arc-0205-b","macAddr":"e8:ba:70:52:bf:80"},{"nodeId":"6","x":"4263","y":"2315","nodeName":"arc-0206-a","macAddr":"e8:ba:70:52:0b:40"},{"nodeId":"7","x":"6578","y":"2924","nodeName":"arc-0206-b","macAddr":"e8:ba:70:52:1e:90"},{"nodeId":"8","x":"8445","y":"2842","nodeName":"arc-0212-a","macAddr":"e8:ba:70:52:ab:e0"},{"nodeId":"9","x":"10110","y":"2802","nodeName":"arc-0210-a","macAddr":"e8:ba:70:61:b3:50"},{"nodeId":"10","x":"7796","y":"1706","nodeName":"arc-0212-b","macAddr":"50:06:04:8d:d0:10"},{"nodeId":"11","x":"8608","y":"1868","nodeName":"arc-0213-a","macAddr":"04:da:d2:74:c8:70"},{"nodeId":"12","x":"10800","y":"1097","nodeName":"arc-0214-a","macAddr":"e8:ba:70:52:bd:80"},{"nodeId":"13","x":"9866","y":"731","nodeName":"arc-0239-a","macAddr":"e8:ba:70:61:a8:80"},{"nodeId":"14","x":"6902","y":"934","nodeName":"arc-0241-a","macAddr":"28:93:fe:d3:8b:20"}]}')
            self.info = data['info']
            self._map = data['map']
            self.wifi = data['wifi']
            pass

        self.maplist = self.graphcreator.create_maplist(self._map)
        self.edges = self.graphcreator.create_edges()
        return (self.maplist, self.edges)
    
    #possible: implement the creating of the mapList here instead of graphCreator
    def get_map(self):
        return (self.maplist, self.edges)
    
    def get_info(self):
        return self.info

    def get_wifi(self):
        return self.wifi

    def get_building(self):
        return self.building

    def get_level(self):
        return self.level