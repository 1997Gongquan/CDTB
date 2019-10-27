import os

# 更新语音对比
dir1="D:/英雄联盟/测试服语音/"
dir2="D:/英雄联盟/voice/voice_code/"
# 第一步，遍历更新文件夹
nameSkins=[]
for hero in os.listdir(dir1):
    for skin in os.listdir(dir1+hero):
        nameSkins.append(hero+"/"+skin)

# 第二步，对比文件，查看是否已经含有，如果已经含有，则删除，不含有保留
for i in nameSkins:
    for voice in os.listdir(dir1+i):
        print(voice)
        oldVoices=[]
        for j in os.listdir(dir2+i):
            oldVoices.append(j)
        if voice in oldVoices:
            os.remove(dir1+i+voice)

# 第三步，删除空文件夹
# for hero in os.listdir(dir1):
#     for skin in os.listdir(dir1+hero):
#         if len(os.listdir(dir1+hero+"/"+skin))==0:
#             os.remove(dir1+hero+"/"+skin)
#     if len(os.listdir(dir1+hero))==0:
#         os.remove(dir1 + hero)
