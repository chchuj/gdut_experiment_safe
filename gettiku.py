import http.cookiejar
import re
import urllib.parse
import urllib.request
import time

answerurl = 'http://biebu.xin/safexam/'
examurl = 'http://222.200.98.165:8090/index.php'
loginurl = 'http://222.200.98.165:8090/exam_login.php'

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
page = opener.open(examurl).read().decode('gb2312')

headers = {
    'Host': '222.200.98.165:8090',
    'Origin': 'http://222.200.98.165:8090',
    'Referer': 'http://222.200.98.165:8090/index.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

postdata = {
    'xuehao': '3114001388',
    'password': '123456',
    'postflag': '1',
    'cmd': 'login',
    'role': '0',
    '%CC%E1%BD%BB': '%B5%C7%C2%BC'
}

data = urllib.parse.urlencode(postdata).encode(encoding='utf-8')
request = urllib.request.Request(url=loginurl, data=data, headers=headers)

try:
    respond = opener.open(request)
    result = respond.read().decode('gbk')
except urllib.request.HTTPError as e:
    print(e)

headers = {
    'Host': '222.200.98.165:8090',
    'Referer': 'http://222.200.98.165:8090/redir.php?catalog_id=6&tikubh=316796&cmd=learning',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}


for i in range(201):
    learningurl = 'http://222.200.98.165:8090/redir.php?catalog_id=6&cmd=learning&tikubh=316796&page='+str(i+1)
    request = urllib.request.Request(url=learningurl, data=None, headers=headers)
    try:
        respond = opener.open(request)
        result = respond.read().decode('gbk')

        index = re.search(r'<div class="shiti-content">(.*?)<div class="fy">', result, re.I | re.M | re.S).span()
        a = result[index[0]:index[1]]
        r = (re.findall(r'<div class="shiti"><h3>(.*?)）</span>', a, re.I | re.M | re.S))
        for x in r:
            ftxt = open("answer22.txt", "a")
            ftxt.write(x+'eleforever'+'\n')

    except urllib.request.HTTPError as e:
        print(e)

    headers = {
        'Host': '222.200.98.165:8090',
        'Referer': 'http://222.200.98.165:8090/redir.php?catalog_id=6&cmd=learning&tikubh=316796&page='+str(i+1),
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    print(i+1)

