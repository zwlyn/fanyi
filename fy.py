# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import urllib
import json
import os
import sys
import codecs
import sys

def multi_translate(content):

    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=http://fanyi.youdao.com/'
    #有道翻译查询入口
    data = {  #表单数据
      'i': content,
      'from': 'AUTO',
      'to': 'AUTO',
      'smartresult': 'dict',
      'client': 'fanyideskweb',
      'doctype': 'json',
      'version': '2.1',
      'keyfrom': 'fanyi.web',
      'action': 'FY_BY_CLICKBUTTION',
      'typoResult': 'false'
     }
    data=urllib.parse.urlencode(data).encode('utf-8')
    #对POST数据进行编码
    response=urllib.request.urlopen(url,data)
    #发出POST请求并获取HTTP响应
    html=response.read().decode('utf-8')
    #获取网页内容，并进行解码解码
    target=json.loads(html)
    #json解析
    print("%s"%target['translateResult'][0][0]['tgt'])
    #输出翻译结果
    return target['translateResult'][0][0]['tgt']


def youdao_translate(content):

    #翻译内容
    if " " in content or content.isascii() is False :
        # 输入为中文或多行时用multi_translate处理
        result = multi_translate(content)
    else:

        url = 'http://fanyi.youdao.com/openapi.do?keyfrom=huacicha&key=199079426&type=data&doctype=json&version=1.1&q=' + content
        data = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
        try:
            print(u'翻译：%s' % data['translation'][0])
            print(u'美式发音：/%s/' % data['basic']['us-phonetic'])
            print(u'英式发音：/%s/' % data['basic']['uk-phonetic'])
            explains = data['basic']['explains']
            print('-' * 25 + u'基本释义' + '-' * 25)
            for i in explains:
                print(u'%s' % i)

            web = data['web']
            print('-' * 25 + u'网络释义' + '-' * 25)
            for i in web:
                print('%s: %s' % (i['key'], ','.join(i['value'])))

            result = "[" + data['basic']['us-phonetic'] + "]  " + data['translation'][0]
        except Exception as e:
            result = multi_translate(content)

    return result



def isEnglish(sentence):
    for word in sentence.split(" "):
        if word.encode('utf-8').isalpha() is False:
            return False

    return True



def isValid(inputline, result):
    # one Chinese and one English is valid
    return isEnglish(inputline) ^ isEnglish(result)



def record_translate(recordFile, inputline, result):
    # 处理 中文输入和英文输入两种情况
    English, Chinese = (inputline, result) if isEnglish(inputline) is True else (result, inputline)
    if isValid(English, Chinese) is True:
        if os.path.exists(recordFile):
            with codecs.open(recordFile, 'r', encoding='utf-8') as f:
                recordDict = json.loads(f.read())
                recordDict.update({English: Chinese})
                with codecs.open(recordFile, 'w', encoding='utf-8') as f:
                    f.write(json.dumps(recordDict, indent=4, ensure_ascii=False)) # ensure_ascii=False 使得中文不是乱码
        else:
            recordDict = {}
            recordDict.update({English: Chinese})
            with codecs.open(recordFile, 'w', encoding='utf-8') as f:
                f.write(json.dumps(recordDict, indent=4, ensure_ascii=False))

if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    RecordFile = os.sep.join([dirname, "record.json"])

    inputList = sys.argv[1:]
    inputLine = ' '.join(inputList)

    result = youdao_translate(inputLine)
    record_translate(RecordFile, inputLine, result)

