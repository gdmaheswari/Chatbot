import requests
import json
class Api:
    def __init__(self):
        pass

    def makeApiRequestForCounrty(self, country_name):
        '''url = "https://covid-193.p.rapidapi.com/statistics"

        headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "bacb2f7897msh94420492b07d300p1c01cajsn113c562a6f2d"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.text)'''

        url = "https://covid-193.p.rapidapi.com/statistics"
        querystring = {"country": country_name}
        headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "bacb2f7897msh94420492b07d300p1c01cajsn113c562a6f2d"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
        js = json.loads(response.text)
        print("******", js)
        result = js.get('response')[0]
        print(result.get('cases'))
        print("*" * 20)
        return result.get('cases') , result.get('deaths'),result.get('tests')


    def makeApiRequestForIndianStates(self,state_name):
        '''url = "https://covid-193.p.rapidapi.com/countries"

        headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "bacb2f7897msh94420492b07d300p1c01cajsn113c562a6f2d"
        }

        response = requests.request("GET", url, headers=headers)
        # print(response.text)'''

        url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
        #string1 = {"state": state_name}
        headers = {
            'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
            'x-rapidapi-key': "bacb2f7897msh94420492b07d300p1c01cajsn113c562a6f2d"
        }
        response = requests.request("GET", url, headers=headers,params=state_name)
        print(response.text)
        js = json.loads(response.text)
        print("******", js)
        # extract an element in the response
        #print(js['state_wise'])
        result = js.get('state_wise')
        result1 =result[state_name]
        print(result1)
        print(result1.get('confirmed'))
        print("*" * 20)
        return result1.get('confirmed'), result1.get('deaths'), result1.get('active')
        #result = js.get('list')
        #return js


    def makeApiWorldwide(self):
        url = "https://covid-19-statistics.p.rapidapi.com/reports/total"
        headers = {
            "x-rapidapi-host": "covid-19-statistics.p.rapidapi.com",
            "x-rapidapi-key": "bacb2f7897msh94420492b07d300p1c01cajsn113c562a6f2d"
        }
        response = requests.request("GET", url, headers=headers)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        result = js.get('data')

        return result

