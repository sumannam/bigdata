# python -m pip install -U pip
# pip install bs4
# pip install beautifulsoup4

from bs4 import BeautifulSoup

html = '<h1 id="title">인천재능대</h1><div class="top"><ul class="menu"><li><a href="http://www.jeiu.ac.kr/login" class="login">로그인</a></li></ul><ul class="brand"><li><a href="http://www.jeiu.ac.kr/computer">인공지능컴퓨터학과<li><a href="http://www.jeiu.ac.kr/academy/">재능대 아카데미</a></li></ul></div>'

soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())
# print(soup.h1)
# print(soup.div)

# print(soup.ul)
# print(soup.find_all("ul"))

# print(soup.li)
# print(soup.find_all("li"))

print(soup.a)

print(soup.find("a"))

print(soup.find_all("a")) # List 타입으로 반환