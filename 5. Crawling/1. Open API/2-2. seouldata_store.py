import urllib.request
import datetime
import json
import pandas as pd

ServiceKey=""

#[CODE 1]
def getRequestUrl(url):    
    req = urllib.request.Request(url)    
    try: 
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print ("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


#[CODE 2]
def getTourismStatsItem(start_index, end_index, year):    
    service_url = "http://openapi.seoul.go.kr:8088"
    parameters = "/" + ServiceKey  #인증키
    parameters += "/" + "json"
    parameters += "/" + "VwsmTrdarSelngQq"
    parameters += "/" + str(start_index)
    parameters += "/" + str(end_index)
    parameters += "/" + str(year)
    url = service_url + parameters
    
    retData = getRequestUrl(url)   #[CODE 1]
    
    if (retData == None):
        return None
    else:
         return json.loads(retData)

#[CODE 3]
def getTourismStatsService(start_index, end_index, year):
    jsonResult = []
    
    for year in range(year, year+1):        
        jsonData = getTourismStatsItem(start_index, end_index, year) #[CODE 2]
        jsonResult.append(jsonData['VwsmTrdarSelngQq']['row'])

    return (jsonResult)

#[CODE 0]
def main():
    jsonResult = []
    result = []
    natName=''

    print("<< 국내 입국한 외국인의 통계 데이터를 수집합니다. >>")
    # output = input('xml or json? : ')
    # start_index =int(input('시작 인덱스? : ')) # 예: 1
    # end_index = int(input('끝나는 인덱스? : '))  # 예: 5
    # year = int(input('검색연도? : '))  # 예: 2020
    
    # jsonResult =getTourismStatsService(start_index, end_index, year) #[CODE 3]
    jsonResult =getTourismStatsService(1, 10, 2020) #[CODE 3]

    print(jsonResult)
    
if __name__ == '__main__':
    main()
