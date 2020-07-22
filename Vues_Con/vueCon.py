import mechanize
import http.cookiejar as cookielib
from bs4 import BeautifulSoup


class Info:

    def __init__(self):
        # Creating Browser
        self.br = mechanize.Browser()

        # Cookie Jar
        cj = cookielib.LWPCookieJar()
        self.br.set_cookiejar(cj)

        # Browser options
        self.br.set_handle_equiv(True)
        self.br.set_handle_gzip(True)
        self.br.set_handle_redirect(True)
        self.br.set_handle_referer(True)
        self.br.set_handle_robots(False)
        self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        self.br.addheaders = [('User-agent', 'Chrome')]

    def login(self, username, password):

        # The site we will navigate into, handling it's session
        self.br.open('https://portal.aiub.edu/')
        # Selecting the Form (nr=Form Index)
        self.br.select_form(nr=0)
        self.br.form['UserName'] = username
        self.br.form['Password'] = password
        # Login
        self.br.submit()

        try:
            page = self.br.open('https://portal.aiub.edu/Student/').read()
            soup = BeautifulSoup(page, 'html.parser')

            name = soup.find(class_='navbar-link')
            name = name.get_text()
            self.name = name
            return name
        except AttributeError:
            return None

    def get_course(self):
        page = self.br.open('https://portal.aiub.edu/Student/GradeReport/ByCurriculum').read()
        soup = BeautifulSoup(page, 'html.parser')
        course = []
        result = []
        tables = soup.find_all(class_='table table-bordered table-compressed')
        for i in range(len(tables)):
            try:
                rows = tables[i + 1].find_all('tr')
            except IndexError:
                pass
            for row in rows:
                col = row.find_all('td')
                course.append(col[1].get_text())
                result.append(col[2].get_text())

        course = [d for d in course if d != '\nCourse in Curriculum\n']
        result = [d for d in result if d != '\nAttended Course/Passing Semester/Grade\n']
        data = {
            'name': course,
            'result': result,
        }
        return data

    def get_gpa(self):
        page = self.br.open('https://portal.aiub.edu/Student/GradeReport/BySemester').read()
        soup = BeautifulSoup(page, 'html.parser')
        tables = soup.find_all(class_='table table-bordered table-compressed')
        row = tables[0].find_all('tr')
        row = row[4].find_all('td')
        return row[2]

    def get_personal_info(self):
        page = self.br.open('https://portal.aiub.edu/Student/Home/Profile').read()
        soup = BeautifulSoup(page, 'html.parser')

        tables = soup.find_all(class_='table')

        col1 = []
        col2 = []

        for i in range(len(tables)):
            try:
                rows = tables[i].find_all('tr')
            except IndexError:
                pass
            for row in rows:
                col = row.find_all('td')
                col1.append(col[0].get_text())
                col = row.find_all('td')
                col2.append(col[1].get_text())

        col1 = [s.strip(' :') for s in col1]
        col2 = [s.strip('\r\n                            ') for s in col2]

        info = {'Name': self.name}
        for key in col1:
            for value in col2:
                info[key] = value
                col2.remove(value)
                break
        return info

    def get_notice(self):
        page = self.br.open('https://www.aiub.edu/category/notices').read()
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
        return notice

    def get_notice_data(self, link):
        page = self.br.open(link).read()
        soup = BeautifulSoup(page, 'html.parser')

        title = soup.find(class_='header-title')
        title = title.get_text()

        body = soup.find(class_='panel-body text-justify')
        data = {
            'Title': title,
            'HTML': body,
        }
        return data



