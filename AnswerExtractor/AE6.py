#############################################
# Type 6:
# lxy
#############################################

from selenium import webdriver

def answer(question, Q_type=6):
    """
    Input :
        question: string
        Q_type: integer
    Outout:
        percentage: 0 or 1, may range from [0, 1] latter.
            (this feature is designed for function 'assemble' in 'QA_system.py')
        answer: string
    """

    percentage = 0
    answer = ''
    if Q_type != 6:
        return [0, '']

    question_str = ["what is","which is","What is","Which is"]
    count =0
    for i in question_str:
        if question.find(i) >= 0:
            n = question.index(i)+len(i)
            break

        count +=1

    if count >= len(question_str):
        print("question format is wrong ! Input your question again!\n")
        return [0, "error"]
    else:
        question_key = question[n:]
        opt= webdriver.ChromeOptions()
        # opt.add_argument('headless')

        # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
        opt.set_headless()
        browser = webdriver.Chrome(options=opt)

        #设置浏览器需要打开的url
        url = "https:/baike.baidu.com"
        browser.get(url)

        #在百度搜索框中输入关键字"python"
        input= browser.find_element_by_id("query")
        input.send_keys("question_key")

        #单击搜索按钮

        browser.find_element_by_id("search").click()

        text = browser.find_element_by_class_name("para").text
        str = "。"
        result_str = text[:text.index(str)]+"。"
        #关闭浏览器
        browser.quit()
        print(result_str)
        return [0.8, result_str]


if __name__ == "__main__":
    print(answer( "what is human"))
