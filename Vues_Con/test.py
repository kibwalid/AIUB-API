import mechanize
import http.cookiejar as cookielib
from bs4 import BeautifulSoup
import numbers
# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]

# The site we will navigate into, handling it's session
br.open('https://portal.aiub.edu/')

# # View available forms for finding form index
# for f in br.forms():
#     print(f)

# Select the second (index one) form (the first form is a search query box)
br.select_form(nr=0)

# User credentials
br.form['UserName'] = '19-41472-3'
br.form['Password'] = 'jimthoe#01A'

# Login
br.submit()


page = br.open('https://www.aiub.edu/category/notices').read()
soup = BeautifulSoup(page, 'html.parser')

events = soup.find(class_='event-list')
title = events.find_all('h2', class_='title')
for i in range(len(title)):
    title[i] = title[i].get_text()

links = []
for link in events.find_all('a', class_='info-link'):
    links.append(link.get('href'))
for i in range(len(links)):
    links[i] = "https://www.aiub.edu" + links[i]

notice = {
    'Title': title,
    'Link': links,
}
print(notice)





# page = br.open('https://portal.aiub.edu/Student/Home/Profile').read()
# soup = BeautifulSoup(page, 'html.parser')
#
# name = soup.find(class_='navbar-link')
#
#
# page = br.open('https://portal.aiub.edu/Student/GradeReport/BySemester').read()
# soup = BeautifulSoup(page, 'html.parser')
# tables = soup.find_all(class_='table table-bordered table-compressed')
#
# col1 = []
# col2 = []
#
# for i in range(len(tables)):
#     try:
#         rows = tables[i].find_all('tr')
#     except IndexError:
#         pass
#     for row in rows:
#         col = row.find_all('td')
#         try:
#             col1.append(col[6].get_text())
#         except IndexError:
#             pass
#
# # col1 = [num for num in col1 if isinstance(num, (int, float))]
# print(col1)
# cg = 0
# for i in range(len(col1)):
#     try:
#         cg = cg + float(col1[i+1])
#     except IndexError:
#         pass
# print(cg/18)
#         col = row.find_all('td')
#         col2.append(col[1].get_text())
#
#
# col1 = [s.strip(' :') for s in col1]
# col2 = [s.strip('\r\n                            ') for s in col2]
#
#
# info = {'name': name}
# for key in col1:
#     for value in col2:
#         info[key] = value
#         col2.remove(value)
#         break
# print(info)
# test.to_csv('aiub.csv', encoding='utf-8-sig')
