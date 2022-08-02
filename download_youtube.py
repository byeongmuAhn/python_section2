from moviepy.editor import *
import pytube
import os.path
# 다운로드 받을 파일 경로
path = 'C:\\workspace\section2\imagedown\\'
def download_mp3(link):
    global path
    yt = pytube.YouTube(link)
    # 유튜브 영상 제목을 추출함, mp3 파일명으로 사용하기 위함
    file_name = yt.title
    full_path = str(path+"/"+str(file_name))
    # 유튜브 영상을 소리만 있는 mp4파일로 다운로드
    yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by( 'abr').desc().first().download(path, str(file_name)+'.mp4')
    # 파일 변환, mp4 -> mp3
    try:
        os.rename(full_path + '.mp4', full_path + '.mp3')
        print("성공")
    except:
        os.remove(full_path + '.mp4')
        print("파일 이미 mp3파일이 있거나, 다른 오류가 발생함")

# 비디오 링크
video_link = 'https://www.youtube.com/watch?v=ykrz-ZRn26I'
download_mp3(video_link)
