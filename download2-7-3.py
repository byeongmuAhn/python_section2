from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = "https://www.inflearn.com/"
res = req.urlopen(url).read()
soup = BeautifulSoup(res, "html.parser")


recommand = soup.select("div.free-courses_content")
#print(recommand)

for i,e in enumerate(recommand,1):
    print(i,e.select_one("a.course_card_front > div.card-content > div.course_title").string)
