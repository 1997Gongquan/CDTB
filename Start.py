import os
import time
from CDTB.cdragontoolbox.wad import Wad
from CDTB.cdragontoolbox.hashes import default_hashfile
import random
def wad_extract(filename, output=None):
    if not os.path.exists(output):
        os.makedirs(output)
    hashfile = default_hashfile(filename)
    wad = Wad(filename, hashes=hashfile.load())
    wad.guess_extensions()
    wad.extract(output, overwrite=True)

def exactDir(dir):
    for file in os.listdir(dir):
        if os.path.isdir(dir+"/"+file):
            exactDir(dir+"/"+file)
        elif ".wad" in file:
            if not os.path.exists("H:/英雄联盟/原始包/"+file):
                os.rename(dir+"/"+file,"H:/英雄联盟/原始包/"+file)
            else:
                os.rename(dir+"/"+file,"H:/英雄联盟/原始包/"+dir.replace("/","_").replace(" ","").replace(":","")+file)
# 解包整个英雄联盟
if __name__ == '__main__':
    fromDir="H:/英雄联盟/原始包/Riot Games/"
    toDir="H:/英雄联盟/lol/"
    exactDir(fromDir)