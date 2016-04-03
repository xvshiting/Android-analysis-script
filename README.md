# Android-analysis-script
## collectapk.py
- 使用方法
 `python collectapk.py XXXXX.txt   XXX/XXX/XXX/apk/`

-  ：自动安装卸载应用，方便检查，按回车卸载应用并安装新的应用。
- 1.将txt文件中出现的`XXXXX.apk` 从`XXX/XXX/XXX/apk`文件中提取到`XXX/XXX/XXX/apk/abnormal`文件夹下，
- 2.并安装首先安装`abnormal`文件下的两个应用，
- 3.此时，可以去手机检查第一个安装的应用，终端上会打印出此应用的包名、版本号等信息，方便记录，
- 4.检查完成后，在终端输入回车，则脚本会自动卸载手机上第一个安装的应用，并自动安装下一个应用，
- 5.此时可以在手机上检查第二个APP，
- 6.终端输入回车后，脚本不仅卸载应用，还会将应用从`abnormal`文件夹下移回到`XXX/XXX/XXX/apk/`文件下，若不想移出当前apk则输入k后按回车
- 需要电脑配置aapt，才能正常运行

## installapk.py
- 使用方法
 `python installapk.py XXX/XXX/XXX/apk/abnormal`
- `collectapk.py`中的安装apk功能，可以直接使用

## getInfo.py
- 使用方法
 `python getInfo.py yourown.excel yidong.excel path`
- 方便生成excel表格
- `yourown.excel` 是在检查过程中，记录的有问题app的excel文件。`yigong.excel`是移动给的所有app信息的excel。`path`是记录结果的文件夹路径
- 脚本会从 `yidong.excel` 中找出 `yourown.excel` 中出现过的MD5对应的信息
- 最后会保存在`path`下生成`result.xls`文件 

