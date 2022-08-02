from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as rep
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# HTML 가져오기
base = "https://search.naver.com/search.naver?where=image&query="
quote = rep.quote_plus("사자")
url = base + quote

res = req.urlopen(url)
savePath ="C:\\workspace\section2\imagedown\\"

try:
    if not(os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed to create directory!!!!!")
        raise

soup = BeautifulSoup(res, "html.parser")
#li_list = soup.select("div.photo_tile._grid > div.thumb > a.link_thumb._imageBox._infoBox > img")
img_list = soup.select("div.img_area > a.thumb._thumb > img")

print("test", img_list)


#main_pack > section.sc_new.sp_nimage._prs_img._imageSearchPC > div > div.photo_group._listGrid > div.photo_tile._grid > div:nth-child(1) > div > div.thumb > a > img
