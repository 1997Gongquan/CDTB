import os
import shutil
if __name__ == '__main__':
    li=os.listdir("H:/test/16000hz/");
    for i in li:
        shutil.rmtree("H:/test/16000hz/"+i+"/assets")
        print(i)
