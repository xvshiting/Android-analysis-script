import pandas as pd
import xlwt
import sys
import openpyxl
import os
#############################################################
#      														#
#    python getInfo.py  yourown.xls   yidong.xls  path      #
#    														#
#    														#
#    														#
#    														#
#############################################################
def writ_to_xls(excel_1,excel_2,write_path):
	df_1=pd.read_excel(excel_1)
	df_2=pd.read_excel(excel_2)
	df_4=df_1.iloc[:,0:1]
	df_4.columns=['A']
	df_2.columns=['A','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w']
	df_2=df_2.iloc[2:,:]
	df_3=pd.merge(df_4,df_2,on='A')
	df_3.to_excel(write_path+os.sep+"result_excel.xls")
	print "done! "+str(write_path+os.sep)+"result_excel.xls"
if __name__ == '__main__':
	writ_to_xls(sys.argv[1],sys.argv[2],sys.argv[3])