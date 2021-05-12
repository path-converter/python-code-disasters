lines=open("music.csv").readlines()
import os
import glob
from shutil import copyfileobj
import ffmpeg
def sortByDate(folderName):
    files=glob.glob(folderName+"*")
    files.sort(key=os.path.getmtime, reverse=False)
    return files
import pyperclip
import webbrowser
from os import path
import subprocess
i=0
ytmp3=input()=="Y"
while ytmp3:
    i+=1
    for line in range(len(lines)):
        print(str(line+1)+"."+lines[line].split(",,")[0])
    idx=int(input())
    url=lines[idx-1].split(",,")[1]
    pyperclip.copy(url)
    if (i==1):
        webbrowser.open("https://ytmp3.cc/youtube-to-mp3/")
files=sortByDate("path/mp3/")
fileNames=open("file_names.txt", "r").readlines()
for file in range(len(files)):
    fileName=fileNames[file].split("-> ")[1].replace("\n", "").removesuffix(" ")+".mp3"
    print(fileName)
    src=files[file]
    dest="path/mp3/"+fileName
    if (not os.path.exists(dest)):
        os.rename(src, dest)
