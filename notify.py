from plyer import notification
import urllib.request
from bs4 import BeautifulSoup
import time


def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "icons8-coronavirus-100.ico", # app icon = "<path>",
        timeout = 3
    )

def getData(url):
    pass
    #r = 
    #return r.text   

if __name__ == "__main__":
    while True:
        # notifyMe("Siddhant", " Let's Stop the spread of the virus together")
        myHtmlData = urllib.request.urlopen('https://www.mohfw.gov.in/').read() # Official website of Ministry of Health and Family Welfare of Gov. of India

        
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr += tr.get_text()
    #        print(myDataStr[1:20],"*"*25)

        myDataStr = myDataStr[1:]
        #print(myDataStr,'/'*25)     
       
        itemList = myDataStr.split("\n\n")
#        j=1
 #       print (itemList[37][8:14])    
        #print(itemList,'&'*25)

        states = ['Delhi'] # You can add more states , and the state which you want
        for item in itemList [0:37]:
             dataList = item.split('\n')
             if dataList[1] in states:
                 print(dataList)
                 nTitle = 'Cases of COVID-19'
                 nText = f"State : {dataList[1]}\nActive cases : {dataList[2]}\nCured : {dataList[3]}\nDeaths : {dataList[4]}\nTotal : {dataList[5]} "
                 notifyMe(nTitle, nText)
                 time.sleep(2)
        nTitle1 = 'Cases of COVID-19'
        nText1 = f"India\nActive cases : {itemList[37][8:14]}\nCured : {itemList[38]}\nDeath : {itemList[39]}\nTotal : {itemList[40]} "                 
        notifyMe(nTitle1, nText1)
        time.sleep(2)
        time.sleep(8)  # it will give alert in regular period , i take it as 3600 Seconds , i.e. 1 Hour 
        