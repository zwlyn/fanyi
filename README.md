# fanyi
+ 句子和单词翻译En ⇋Ch
+ 支持 python2.7、python3.x
+ 极简实现没有使用第三方库

# 功能如下
## 1.支持翻译单个英语单词
```
python fy.py hello
```
```
翻译：你好
美式发音：/helˈō/
英式发音：/həˈləʊ/
-------------------------基本释义-------------------------
int. 喂；哈罗，你好，您好
n. 表示问候， 惊奇或唤起注意时的用语
n. (Hello) 人名；（法）埃洛
-------------------------网络释义-------------------------
Hello: 你好,您好,哈啰
Hello Kitty: 凯蒂猫,昵称,吉蒂猫
Hello Bebe: 哈乐哈乐,乐扣乐扣
```
## 2.支持翻译英文长句
```
python fy.py hello world
>>你好，世界
```

## 3.支持翻译中文(包括长句)
```
python fy.py 你好
>>hello
```

## 4.会存储翻译的历史记录到文件同级的 record.json中
例如：
```
  {
      "hello": "[helˈō]  你好",
      "Hello world": "你好世界"
  }
```

## 5.通过设置别名可以实现
```
fy 你好
>>hello
```
这样便利的使用方式
### windows用户：
只针对powershell
#### 1.找到Microsoft.PowerShell_profile.ps1文件的位置
```
$profile
>>C:\Users\xx\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
```
#### 2.向Microsoft.PowerShell_profile.ps1添加
```
function fy {python 文件路径\fy.py $args}
```



### linux用户：
在.bashrc中添加：
```
alias fy='python 文件路径/fy.py'
```

