from request_handler import RequestHandler
import pandas as pd

class Fetcher:
    def __init__(self):
        self.rh = RequestHandler()

    def statistics(self):
        stat = self.rh.get_statistics()
        stat = {stat[i] : [stat[i]] for i in stat.keys()}
        return pd.DataFrame(stat)
        
    def coutries_data(self):
        data = self.rh.get_countries()
        for i in range(len(data)):
            countryInfo = data[i]["countryInfo"]
            for key in countryInfo.keys():
                new_key = "countryInfo__{}".format(key)
                data[i][new_key] = countryInfo[key]
            del data[i]["countryInfo"]
        
        ret = {i:[] for i in data[0].keys()}
        for i in range(len(data)):
            for key in data[i].keys():
                ret[key].append(data[i][key])

        return pd.DataFrame(ret) 

    def coutry_data(self, country="Bangladesh"):
        data = self.rh.get_country(country)
        
        countryInfo = data["countryInfo"]
        for key in countryInfo.keys():
            new_key = "countryInfo__{}".format(key)
            data[new_key] = countryInfo[key]
        del data["countryInfo"]
        
        ret = {i:[data[i]] for i in data.keys()}

        return pd.DataFrame(ret) 

    def countries_historical_data(self):
        data = self.rh.get_countries_historical()

        ret = {i:[] for i in data[0].keys()}
        ret['cases'] = []
        ret['deaths'] = []
        for i in range(len(data)):
            timeline = list(set(list(data[i]['timeline']['cases'].keys()) + \
                            list(data[i]['timeline']['deaths'].keys())))
            
            for each_timeline in timeline:
                if each_timeline in data[i]['timeline']['cases'].keys():
                    ret['cases'].append(data[i]['timeline']['cases'][each_timeline])
                else:
                    ret['cases'].append(0)

                if each_timeline in data[i]['timeline']['deaths'].keys():
                    ret['deaths'].append(data[i]['timeline']['deaths'][each_timeline])
                else:
                    ret['deaths'].append(0)
            
                ret['timeline'].append(each_timeline)

                for key in data[i].keys():
                    if key != 'timeline':
                        ret[key].append(data[i][key])
        
        return pd.DataFrame(ret) 

  

    def country_historical_data(self, country):
        data = self.rh.get_country_historical(country)

        ret = {i:[] for i in data.keys()}
        ret['cases'] = []
        ret['deaths'] = []

        timeline = list(set(list(data['timeline']['cases'].keys()) + \
                    list(data['timeline']['deaths'].keys())))
            
            
        for each_timeline in timeline:
            if each_timeline in data['timeline']['cases'].keys():
                ret['cases'].append(data['timeline']['cases'][each_timeline])
            else :
                ret['cases'].append(0)

            if each_timeline in data['timeline']['deaths'].keys():
                ret['deaths'].append(data['timeline']['deaths'][each_timeline])
            else :
                ret['deaths'].append(0)
        
            ret['timeline'].append(each_timeline)

            for key in data.keys():
                if key != 'timeline':
                    ret[key].append(data[key])
        
        return pd.DataFrame(ret) 



if __name__ == '__main__':
    f = Fetcher()
    print(f.country_historical_data("China"))

