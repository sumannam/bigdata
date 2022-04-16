import os
import sys
import urllib.request
import datetime
import time
import json
import pandas as pd

#서울열린광장에서 받은 개인 인증키
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


#[CODE 2] "서울 열린데이터 광장" : 한 page에 5개만 display됨. 
def getPage(start):    
    url = 'http://openapi.seoul.go.kr:8088/' + ServiceKey+'/json/ChunmanFreeSuggestions/%d/%d' % (start, start+4)    
    retData = getRequestUrl(url)   #[CODE 1]
    
    if (retData == None):
        return None
    else:
         return json.loads(retData)


#[CODE 3]  "서울 열린데이터 광장" : 최대 1000개까지만 제공
def getItemsAll():
    result = []
    for i in range(1000//5):
        jsonData = getPage(i*5 +1) #[CODE 2]        
        if (jsonData['ChunmanFreeSuggestions']['RESULT']['CODE'] == 'INFO-100'):
            print("인증키가 유효하지 않습니다!!")
            return

        if(jsonData['ChunmanFreeSuggestions']['RESULT']['CODE'] == 'INFO-000'):
            for i in range(5):
                SN = jsonData['ChunmanFreeSuggestions']['row'][i]['SN']
                TITLE = jsonData['ChunmanFreeSuggestions']['row'][i]['TITLE']
                CONTENT_link = jsonData['ChunmanFreeSuggestions']['row'][i]['CONTENT']
                DATE = jsonData['ChunmanFreeSuggestions']['row'][i]['REG_DATE']
                result.append([SN, TITLE, CONTENT_link, DATE])
    return result


#[CODE 0]
def main():
    jsonResult = []
    result = []

    print("<< 현재 기준 '민주주의 서울 자유제안’ 데이터 1000개를 수집합니다. >>")
    
    result = getItemsAll() #[CODE 3]
 
    #파일저장 : csv 파일   
    columns = ["SN", "TITLE", "CONTENT_link", "DATE"]
    result_df = pd.DataFrame(result, columns = columns)
    result_df.to_csv('./민주주의서울자유제안.csv',  index=False, encoding='cp949')

    
if __name__ == '__main__':
    main()
