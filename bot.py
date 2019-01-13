from bs4 import BeautifulSoup
import requests

base_url = "http://questions.menstrupedia.com"

def make_query():
    user_query = input ("Input your query regarding menstrutation: ")
    query = user_query.split(" ")
    query = "+".join(query)
    return query

def fetch_questions(query):
    url = base_url + "/search/?q="+query+"&Submit=search&t=question"
    page  = requests.get(url)
    data = BeautifulSoup(page.content, "html.parser")
    ques = data.findAll(class_="question-summary-wrapper")

    c=0
    url_list = []
    string_list = []

    if len(ques) == 0:
        print ("No questions found")
        return ("Result not found")

    for i in ques:
        qstring = ""

        if c == 5:
            break
        c+=1
        Q = i.find("h2").get_text()
        h = i.find("a")
        ans_url = (base_url + h["href"]+"\n")
        url_list.append(ans_url)
        qstring += "*" + Q + "*" + "\n"
        qstring += h["title"]+"\n" + "\n"
        qstring += "*Answer link* " + ans_url+ "\n"
        string_list.append(qstring)
    return (url_list, string_list)

def fetch_answer(url_list):
    user_ans = int(input("Which question number answere you want "))
    ans_page = requests.get(url_list[user_ans-1])
    ans_data = BeautifulSoup(ans_page.content, "html.parser")
    ans = ans_data.findAll(class_="answer-body")

    if len(ans) == 0:
        print ("No Answer found")

    j = 0
    for i in ans:
        if (j==3):
            break
        j += 1
        A = i.find("p").get_text()
        print (str(j)+ ". " + A + "\n")
        print ("\n$$$----------------------hyeeee Cool Answer-----------------------------------------$$$\n")


if __name__ == "__main__":
    query = make_query()
    question_urls = fetch_questions(query)[0]
    if len(question_urls) > 0:
        fetch_answer(question_urls)