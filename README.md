# 动机
    * 提高快速查找函数以及使用
    * 支持语言Python


# 答案类型
    1. How? || Do something.
    2. What?
    3. Can?
    4. Why?
    5. Is there? 

# 工作框架
      input:一个问题
            ||
            ||（深度学习或啥方法）
            \/
       给出调用哪个模块的“标识”（ex:1给出函数接口、2某种语言实现某种算法或功能、3编译错误、4函数属于哪个包）
       case:标识
          模块1:
                answer+=给出函数接口;
          模块2:
                answer+= 某种语言实现某种算法或功能;
          ……
       
       output:汇总answer然后输出；

# 数据库来源
    * stackoverflow上找问题：
    可参考：
         stackoverflow上Python相关回答整理翻译 https://github.com/wklken/stackoverflow-py-top-qa
    * Pipy网站上建立索引
    * https://languageresources.github.io/tags/%E6%95%B0%E6%8D%AE%E9%9B%86/

# START
```bash
$ pip install -r requirements.txt
$ python server.py
```

# Introduction

1. 输入问题与问题库（StackOverflow）的相似度计算？ 【相似度，link】
2. 根据link，找到vote最高的。 【返回能否找到，vote，string】
3. 如果没找到，或者1里面相似度太低。 【分类结果】
对问题做分析。基于5类答案类型总结能回答的问题。
4. 判断What? 回答 什么东西是什么。 【string，能不能回答】

5. 判断How？ 回答 流程 1. 2. 3. 4. (词性标注) 【TODO】
6. 判断Can? Is there?  回答 Yes 或者No。并给出示例。  【Yes. No.】
7. Why? 【】

c\\xc3\\xb1'            C#
\\xc3\\xbbnet           .net
c\\xc3\\xa7\\xc3\\xa7   C++
