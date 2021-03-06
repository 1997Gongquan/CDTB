#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8日 2:00
# @Author  : Virace
# @Email   : Virace@aliyun.com
# @File    : main.py

import os
import configparser
import time
from CDTB.cdragontoolbox.wad import Wad
from CDTB.cdragontoolbox.hashes import default_hashfile


def wad_extract(filename, output=None):
    if not output:
        output = os.path.splitext(filename)[0]
    if not os.path.exists(output):
        os.mkdir(output)
    hashfile = default_hashfile(filename)
    wad = Wad(filename, hashes=hashfile.load())
    wad.guess_extensions()
    wad.extract(output, overwrite=True)


config = configparser.ConfigParser()
config.read('.\config.ini', encoding="utf-8")

# 语音文件位置
PATH = os.path.join(config.get("extract", "game_path"), r'')
# for i in os.listdir(PATH):
#     if "zh_CN" not in i:
#         os.remove(PATH+"/"+i)
# 输出目录
OUTER = config.get("extract", "output_path")
# RExtractorConsole CLI
EXTRA_EXE = config.get("extract", "recli")

TIME=config.get("extract","last_time")
# 取出中文语音并派出SG开头文件
file_list = [item for item in os.listdir(PATH)]

# 英雄列表初始化
champions = list()
################## 第一步解包WAD ##################
#
# 遍历语音文件
for item in file_list:
    # 取出英雄名字
    champion_name =  item.split('.')[0]
    # 拼接输出目录
    item_outer = os.path.join(OUTER, champion_name)
    # 拼接语音wad文件位置
    item_path = os.path.join(PATH, item)
    if int(time.strftime("%Y%m%d",time.localtime(os.stat(item_path).st_mtime)))>int(TIME):
        print(champion_name)
        # 加入英雄名字列表
        champions.append(champion_name)
        # wad文件解包
        try:
            wad_extract(item_path, item_outer)
            pass
        except:
            print("出错")
#
# ################## 第二步解包WPK ##################
#
# 遍历英雄名字
for item in champions:
    # if len(os.listdir(OUTER+"/"+item))==1:
    if len(os.listdir(OUTER+"/"+item))>0:
        # 拼接皮肤目录
        skin_paths = os.path.join(OUTER, item, r'assets\sounds\wwise2016\vo\zh_cn\characters\%s\skins' % item.lower())
        # 遍历皮肤目录 base 、 skin01 、 skin02 等等
        try:
            for skin_item in os.listdir(skin_paths):
                # 拼接皮肤目录
                skin_path = os.path.join(skin_paths, skin_item)
                # 遍历文件并只取出wpk文件
                for item_wpk in [i for i in os.listdir(os.path.join(skin_path)) if i.split('.')[-1] == 'wpk']:
                    # 用RExtractor解包
                    os.system('%s %s %s /soundformat:wav' % (EXTRA_EXE, os.path.join(skin_path, item_wpk), os.path.join(OUTER, item, skin_item)))
        except:
            print(skin_paths+"打开失败")

# 删除assets目录 也就是wpk bnk文件目录，因为用不到了
for item in champions:
    temp_path = os.path.join(OUTER, item, 'assets')
    os.system('rd /q /s %s' % temp_path)
