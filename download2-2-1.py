import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl ="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAyMjZfMjE2%2FMDAxNjQ1ODQ5NjAxNTA1.2lqntDk_ocYTLckKZfARn_clTSuuwqgVFwGeqAeu9Vgg.paCSBMVeGWOsAy0f09MgSl3LvdYn-eeJKEfPhISbSaIg.JPEG.kwskorea52%2Fkb_buddies_2008-03.jpg"
htmlURL ="http://google.com"

savePath1 ="C:/workspace/section2/test1.jpg"
savePath2 ="C:/workspace/section2/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL, savePath2)

print("다운로드 완료!")
