import requests
import Constants

def isSiteOnline(siteUrl):
    response = requests.get(siteUrl, timeout=10)
    if(response.status_code==200):
        return True
    else:
        return False

if(isSiteOnline(Constants.BASE_URL)==True):
    print('Website je online')
else:
    print('Website nije online')

