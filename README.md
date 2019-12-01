# 动机
    * 提高快速查找函数以及使用
    * 支持语言Python


# 答案类型
    1. 给出函数接口 (返回sort(x,x), samples)
    2. 某种语言实现某种算法或功能 (code blocks)
    3. 编译错误 (install xx packages)
    4. 函数属于哪个包 (in xx packges)
    5. 其他
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

# 工作划分
    1. 答案分类模型实现 (Multi)<-->
    2. 系统搭建 (Single)<-->
    3. 第X种类型特征提取 (Multi)<-->
    4. 第X种回答格式 (Multi)<-->

# 建立知识库
    最终格式

# 数据库来源
    * stackoverflow上找问题：
    可参考：
         stackoverflow上Python相关回答整理翻译 https://github.com/wklken/stackoverflow-py-top-qa
    * Pipy网站上建立索引


