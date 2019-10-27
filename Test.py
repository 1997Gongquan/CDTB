import os
from CDTB.cdragontoolbox.wad import Wad
from CDTB.cdragontoolbox.hashes import default_hashfile
import json
def wad_extract(filename, output=None):
    if not output:
        output = os.path.splitext(filename)[0]
    if not os.path.exists(output):
        os.mkdir(output)
    hashfile = default_hashfile(filename)
    wad = Wad(filename, hashes=hashfile.load())
    wad.guess_extensions()
    wad.extract(output, overwrite=True)


def renameSkin():
    temp=json.load(open("G:/temp/plugins/rcp-be-lol-game-data/global/default/v1/championperkstylemap.json"));
    dir="G:/temp/plugins/rcp-be-lol-game-data/global/default/v1/champion-splashes/uncentered/"
    dir="G:/博客/lol/allSkin/champion-tiles/"
    for i in temp:
        try:
            os.rename(dir+str(i["championId"]),dir+i["championName"])
        except:
            print(i)
def renameSkinName():
    dir1="G:/博客/lol/allSkin/champion-tiles/"
    for i in os.listdir(dir1):
        for j in os.listdir(dir1+i):
            a = len(j.split(".jpg")[0]) - 3;
            s=""
            while a<len(j.split(".jpg")[0]):
                s=s+j[a]
                a=a+1
            os.rename(dir1+i+"/"+j,dir1+i+"/"+str(int(s))+".jpg")
def readSkinName():
    # dir="G:/博客/lol/fontconfig_zh_cn.txt"
    cn_map={}
    dir="G:/博客/lol/00.txt"
    f=open(dir,'r',encoding='UTF-8')
    a=f.read()
    s=a.split("\n")
    # f1 = open("G:/博客/lol/fontconfig_zh_cn1.txt", 'w', encoding='UTF-8')
    for i in s:
        cn=i.replace("  ", " ").split(" = ")[1].replace("\"", "").split(" ")
        print(cn)
    # f1.close()
# if __name__ == '__main__':
#     # wad_extract("C:/Game/WeGame/WeGameApps/英雄联盟/Game/DATA/FINAL/Localized/Global.zh_CN.wad.client", "G:/temp2/")
#     # renameSkin()
#     renameSkinName()
#     # readSkinName()
if __name__ == '__main__':
    # for i in os.listdir("G:/博客/lol/voice/voice/"):
    #     lis=os.listdir("D:/test/")
    #     if i not in lis:
    #         print(i)
    readSkinName()