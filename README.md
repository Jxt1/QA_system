# 动机
    * NLP 2019 Fall
    * 方便程序员查找资料

# Installation
解压data/stackoverflow_index.txt.zip文件。
注意： 在data/stackoverflow_index.txt文件中有两行“冗余”可能会影响处理（问题编号476600与476636之间），

解压数据删掉这两个问题之间多余的两行即可。
```bash
$ pip install -r requirements.txt
$ python server.py
```

输入例子：
```bash
How Can I format a nuber into a string with leading zeros
Can I create a column of nvarchar(MAX) using FluentMigrator?
Why do table names start with "dbo" in SQL Server
What is the difference between map and collect in Ruby?
exactly what does env do in Bash?
What is the optimal length for user password salt?
Alarm Manager Example
```

如果缺少english.pickle
```bash
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
```
然后在All Packages中选择punkt下载。

# 答案类型
    1. How? || Do something.
    2. Yes or No
    3. Why?
    4. Compare
    5. What do
    6. What
    7. others
# 数据库来源
    * stackoverflow上找问题：
    可参考：
         stackoverflow上Python相关回答整理翻译 https://github.com/wklken/stackoverflow-py-top-qa
    * Pipy网站上建立索引
    * https://languageresources.github.io/tags/%E6%95%B0%E6%8D%AE%E9%9B%86/
