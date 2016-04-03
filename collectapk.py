#coding=utf-8
###################################################
#                                               ##
#  python collectapk.py  txt路径    apk所在文件夹 ##
#                                               ##
##################################################
import re
import os
import sys
import shutil
import installapk
def mkdirs(path): 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 创建目录操作函数
        os.makedirs(path)
        # 如果不存在则创建目录
        print path + "build successful"
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path + "catagery already exists"
        return False
textname=sys.argv[1]
ApkPath=sys.argv[2]
f=open(textname,"r")
text=f.readlines()
f.close
reg = r'[0-9A-Za-z]+.apk'
u= re.compile(reg)
ApkName=[]
for line in text:
	name=re.findall(u,line)
	if len(name)!=0 :
		ApkName.append(name)
#新建文件夹
Abnormal_Apk_path=ApkPath+os.sep+"Abnormal_APK"
mkdirs(Abnormal_Apk_path)
for name in ApkName:
	temppath=ApkPath+os.sep+name[0]
	newppath=Abnormal_Apk_path+os.sep+name[0]
	shutil.move(temppath,newppath) 
	print "move successful---"+name[0] 
print "done!!"
installapk.install_apk(Abnormal_Apk_path)





