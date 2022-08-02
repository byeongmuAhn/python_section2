import pytube
import os
import subprocess


sourceUrl = input("다운받을 주소는? ")

yt = pytube.YouTube(sourceUrl) #다운받을 동영상 URL 지정

vids= yt.streams.all()

#영상 형식 리스트 확인
for i in range(len(vids)):
    print(i,'. ',vids[i])

vnum = int(input("다운 받을 화질은? "))

parent_dir = "C:\youtube"
vids[vnum].download(parent_dir) #다운로드 수행


default_filename = vids[vnum].default_filename


new_filename = os.path.splitext(default_filename)[0] + ".mp3"


subprocess.call(['ffmpeg', '-i',                 #cmd 명령어 수행
    os.path.join(parent_dir, default_filename),
    os.path.join(parent_dir, new_filename)
])

print('동영상 다운로드 및 mp3 변환 완료!')
