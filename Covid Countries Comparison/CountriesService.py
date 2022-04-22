import requests

class CountriesService:
    @staticmethod
    def get_countries():
        tabresult=[]
        result = requests.get(f"https://api.covid19api.com/countries").json()
        #print(result)

        for x in result:
            tabresult.append(x['Country'])

            tabresult.sort()

            return tabresult

