import urllib.request


request = urllib.request.Request(URL)

search_addr="https://www.google.co.kr.do?query="
search word=str
search_Word_enc=urllib.parse.quote(search_word) #get요청시 url 인코딩
URL=search_addr+search_Word_enc
request=urllib.request.Request(URL)
response = urllib.request.urlopen(req)
status_code = response.getcode()
html_data=response.read()



def keyword(list): #keyword list 합치기
    str=""
    num=len(list) # keyword 개수
    for i in list:
        str+=i
        str+=" "
    return str

def search(str):





