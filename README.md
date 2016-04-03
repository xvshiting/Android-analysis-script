# Android-analysis-script
## collectapk.py
- 使用方法
 `python collectapk.py XXXXX.txt   XXX/XXX/XXX/apk/`

- 作用 ：自动安装卸载应用，方便检查，按回车卸载应用并安装新的应用。
- 1.将txt文件中出现的XXXXX.apk 从XXX/XXX/XXX/apk文件中提取到XXX/XXX/XXX/apk/abnormal文件夹下，
- 2.并安装首先安装abnormal文件下的两个应用，
- 3.此时，可以去手机检查第一个安装的应用，终端上会打印出此应用的包名、版本号等信息，方便记录，
- 4.检查完成后，在终端输入回车，则脚本会自动卸载手机上第一个安装的应用，并自动安装下一个应用，
- 5.此时可以在手机上检查第二个APP，
- 6.终端输入回车后，脚本不仅卸载应用，还会将应用从abnormal文件夹下移回到XXX/XXX/XXX/apk/文件下，若不想移出当前apk则输入k后按回车
- 

