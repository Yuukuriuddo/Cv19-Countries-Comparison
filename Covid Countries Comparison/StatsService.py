import requests

from MyModel import ResultModel

class StatsService:
    @staticmethod
    def get_stats(country):
        result = requests.get(f"https://api.covid19api.com/total/dayone/country/{country}").json()
        if(len(result)==0):
            return False
        lastindex=len(result)-1
        rs = ResultModel(country,
        result[lastindex]['Confirmed'],
        result[lastindex]['Deaths'],
        result[lastindex]['Date'],
        result[lastindex]['Active']
        )
        return rs


    @staticmethod
    def get_deaths_for_all_countries(countriesList):
        tab=[]
        stats:ResultModel

        for c in countriesList:
            stats = StatsService.get_stats(c)
            tab.append(stats.mystats["deaths"])

        return tab