import http.cookiejar
import re
import urllib.request


def iserror(page):  # 若验证码正确，返回False

    if (re.search(r'<br>A\.&nbsp', page, re.I | re.M)) is not None:
        return 'A'
    if (re.search(r'<br>B\.&nbsp', page, re.I | re.M)) is not None:
        return 'B'
    if (re.search(r'<br>C\.&nbsp', page, re.I | re.M)) is not None:
        return 'C'
    if (re.search(r'<br>D\.&nbsp', page, re.I | re.M)) is not None:
        return 'D'
    if (re.search(r'正确答案是 A', page, re.I | re.M)) is not None:
        return 'A'
    if (re.search(r'正确答案是 B', page, re.I | re.M)) is not None:
        return 'B'
    if (re.search(r'正确答案是 C', page, re.I | re.M)) is not None:
        return 'C'
    if (re.search(r'正确答案是 D', page, re.I | re.M)) is not None:
        return 'D'
    if (re.search(r'标准答案：    A', page, re.I | re.M)) is not None:
        return 'A'
    if (re.search(r'标准答案：    B', page, re.I | re.M)) is not None:
        return 'B'
    if (re.search(r'标准答案：    C', page, re.I | re.M)) is not None:
        return 'C'
    if (re.search(r'标准答案：    D', page, re.I | re.M)) is not None:
        return 'D'
    if (re.search(r'标准答案：    正确', page, re.I | re.M)) is not None:
        return '1'
    if (re.search(r'标准答案：    错误', page, re.I | re.M)) is not None:
        return '0'
    if (re.search(r'正确答案是 正确', page, re.I | re.M)) is None:
        return '0'
    else:
        return '1'


while True:
    score = 0
    xuehao = input('请输入你的学号：\n')
    answerurl = 'http://biebu.xin/safexam/'
    examurl = 'http://222.200.98.165:8090/index.php'
    loginurl = 'http://222.200.98.165:8090/exam_login.php'

    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    page = opener.open(examurl).read().decode('gbk', errors='ignore')

    headers = {
        'Host': '222.200.98.165:8090',
        'Origin': 'http://222.200.98.165:8090',
        'Referer': 'http://222.200.98.165:8090/index.php',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }

    postdata = {
        'xuehao': xuehao,
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
        'Connection': 'keep-alive',
        'Host': '222.200.98.165:8090',
        'Referer': 'http://222.200.98.165:8090/exam_login.php',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36i/537.36'
    }
    request = urllib.request.Request(url=examurl, data=None, headers=headers)
    respond = opener.open(request)
    result = respond.read().decode('gbk')

    headers = {
        'Connection': 'keep-alive',
        'Host': '222.200.98.165:8090',
        'Referer': 'http://222.200.98.165:8090/index.php',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36i/537.36'
    }
    enterurl = 'http://222.200.98.165:8090/redir.php?catalog_id=6'
    request = urllib.request.Request(url=enterurl, data=None, headers=headers)
    respond = opener.open(request)

    kaoshiurl = 'http://222.200.98.165:8090/redir.php?catalog_id=6&cmd=kaoshi_chushih&kaoshih=317797'
    headers = {
        'Connection': 'keep-alive',
        'Host': '222.200.98.165:8090',
        'Referer': 'http://222.200.98.165:8090/redir.php?catalog_id=6',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36i/537.36'
    }
    request = urllib.request.Request(url=kaoshiurl, data=None, headers=headers)
    respond = opener.open(request)
    quessheet = respond.read().decode('gbk')

    answer = open('answer.txt')
    answer = answer.read()

    datiurl = 'http://222.200.98.165:8090/redir.php?catalog_id=6&cmd=dati'

    headers = {
        'Host': '222.200.98.165:8090',
        'Origin': 'http://222.200.98.165:8090',
        'Referer': 'http://222.200.98.165:8090/redir.php?catalog_id=6&cmd=dati',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }

    for i in range(10):
        postdata = {
            'runpage': '0',
            'page': '',
            'direction': '1',
            'tijiao': '0',
            'postflag': '1',
            'autosubmit': '0'
        }
        index = re.search(r'<form method="post" id="dati">(.*?)<div class="nav">', quessheet, re.I | re.M | re.S).span()
        a = quessheet[index[0]:index[1]]
        r = (re.findall(r'<div class="shiti"><h3>(.*?)</h3><ul class=', a, re.I | re.M | re.S))

        for x in range(10):
            xx = r[x]
            try:
                result = re.search(r'' + xx[3::] + '(.*?)' + 'eleforever', answer, re.I | re.M | re.S)
                if result is not None:
                    reindex = result.span()
                    imp = answer[reindex[0]:reindex[1]]
                    temdaan = iserror(imp)
                    postdata['ti_' + str(x + i * 10 + 1)] = temdaan
                    score += 1
                    print(str(xx)+'选择'+temdaan)
            except:
                continue

        postdata['page'] = str(i)
        data = urllib.parse.urlencode(postdata).encode(encoding='utf-8')
        request = urllib.request.Request(url=datiurl, data=data, headers=headers)
        respond = opener.open(request)
        quessheet = respond.read().decode('gbk')

    print('得分：' + str(score))
