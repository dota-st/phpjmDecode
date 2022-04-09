'''
Author: dota_st
Date: 2022-03-23 17:27:50
blog: www.wlhhlc.top
'''
import shutil
import os
import re
import sys

def decode(fileName):
    tempFile = "temp.php"
    originContent = open(fileName,'r').read()
    dataList = re.findall('(\<\?php.*?\>)',originContent.replace('\n', ' ').replace('\r', ' '))
    fileResult = ""
    for data in dataList:
        flag = 0
        while(1):
            Content = open(fileName,'r').read()
            if(flag == 0):
                Content = data
                flag = 1
            if len(Content) <= 10:
                Content = data
            if 'eval' in Content:
                tempContent = Content.replace("eval","echo")
                open(fileName,'w').write(tempContent)
                os.system("php {fileName} > {tempFile}".format(fileName=fileName,tempFile=tempFile))
                shutil.copyfile(tempFile, fileName)
            else:
                try:
                    result = re.findall('(eval\(.*?\);)',data)[0]
                    result = data.replace(result,"echo('<?php ');"+Content)
                    open(fileName,'w').write(result)
                    shutil.copyfile(fileName, tempFile)
                    os.system("php {tempFile} > {fileName}".format(tempFile=tempFile,fileName=fileName))
                    os.unlink(tempFile)
                    break
                except:
                    open(fileName,'w').write(data)
                    shutil.copyfile(fileName, tempFile)
                    os.system("php {tempFile} > {fileName}".format(tempFile=tempFile,fileName=fileName))
                    os.unlink(tempFile)
                    break
        fileContent = open(fileName,'r').read()
        fileResult += fileContent
    open(fileName,'w').write(fileResult)

def banner():
    logo = r"""
       .__               __          ________                         .___      
______ |  |__ ______    |__| _____   \______ \   ____  ____  ____   __| _/____  
\____ \|  |  \\____ \   |  |/     \   |    |  \_/ __ _/ ___\/  _ \ / __ _/ __ \ 
|  |_> |   Y  |  |_> >  |  |  Y Y  \  |    `   \  ___\  \__(  <_> / /_/ \  ___/ 
|   __/|___|  |   __/\__|  |__|_|  / /_______  /\___  \___  \____/\____ |\___  >
|__|        \/|__|  \______|     \/          \/     \/    \/           \/    \/ 

usage:  python3 phpjmDecode.py [fileName]
Powered by dota_st
Blog's: https://www.wlhhlc.top/
"""
    print(logo)

def main():
    originFileName = sys.argv[1]
    TempFileName = originFileName.split('.')[0]
    fileName = TempFileName+".de.php"
    shutil.copyfile(originFileName, fileName)
    while(1):
        result = open(fileName,'r').read()
        print(f"\033[1;32m====================...Decrypting...========================\033[0m"+"\n")
        print(result+"\n")
        print(f"\033[1;32m============================================================\033[0m")
        flag = re.findall(r'({[0-9]})',result)
        if flag:
            decode(fileName)
        else:
            print(f"\033[1;34m[*]Decryption complete!\033[0m")
            break

if __name__ == '__main__':
    banner()
    main()