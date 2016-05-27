#coding=utf-8
import re
import os
import sys
import zipfile
import shutil
import  xml.dom.minidom
import time
def install_apk(path):
	adb_install="adb install "
	install_string=""
	files = os.listdir(path)
	reg = r'.*apk'
	u= re.compile(reg)
	times=0;
	packageName=[1,2]
	version=[1,2]
	fileName=[1,2]
	for f in files:
		if re.match(u,f):
			print f
			install_string=adb_install+path+os.sep+f
			p=os.popen("aapt dump badging "+path+os.sep+f+" |grep package")
			a=p.read().decode('utf8')
			packageName[1]=packageName[0]
			version[1]=version[0]
			fileName[1]=fileName[0]
			packageName[0]=getpackageName(a)
			version[0]=getversion(a)
			fileName[0]=str(f)
			print  "-------正在安装-------"
			print " 文件名:"+str(fileName[0])
			time.sleep(5)
			p_install=os.popen(install_string)
			time.sleep(5)
			print "版本号：" +str(version[0])
			print "包命： " +str(packageName[0])
			if times==0:
				times=times+1
				time.sleep(30)
				continue
			x=raw_input("按回车删除"+"\n" +str(packageName[1])+"\n"+str(version[1])+"\n"+fileName[1]+"\n安装下一个APK  若疑似恶意 可输入k后回车 将应用保留在当前文件：")
			print "-------正在删除应用-----"+str(packageName[1])
			uninstall_string="adb uninstall "+str(packageName[1])
			p_uninstall=os.popen(uninstall_string)
			time.sleep(5)
			if x!="k":
				shutil.move(path+os.sep+fileName[1],path+os.sep+".."+os.sep)#安装卸载后的应用移出当前文件夹
			else:
				print("已保存！")	


def getpackageName(data):
	reg=r'package: name=\'(.+)\' versionCode'
	u= re.compile(reg)
	g=u.match(data)
	return g.group(1)
	

def delete_apk():
	pass
def getversion(data):
	reg=r'.* versionName=\'(.+)\''
	u= re.compile(reg)
	g=u.match(data)
	return g.group(1)
if __name__ == '__main__':
	install_apk(sys.argv[1])




