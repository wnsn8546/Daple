import json
import urllib.error
import urllib.parse
import urllib.request
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "daple.settings")
import django
django.setup()
from stores.models import Store

client_id = "uCCiykUMH5IF4JADGgWL"
client_secret = "mD53NEgVgg"
encText = urllib.parse.quote("우동")
url = "https://openapi.naver.com/v1/search/local?query=" + encText +"&display=10&start=1&sort=random"# JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if rescode == 200:
    response_body = response.read()
    response_body = response_body.decode('utf-8')
    response_body = json.loads(response_body)
    temp = response_body["items"]
    for i in range(len(temp)):
        db_save = Store(store_name=temp[i]["title"], store_address=temp[i]["address"], store_x=temp[i]["mapx"],
                        store_y=temp[i]["mapy"])
        db_save.save()
    print(temp[0]["address"])
    result = []
    for i in range(len(temp)):
        result.append(temp[i]["address"])
    print(result)
else:
    print("Error Code:" + rescode)
# Create your views here.