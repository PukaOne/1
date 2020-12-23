'''
Author: your name
Date: 2020-12-21 19:55:59
LastEditTime: 2020-12-23 11:01:58
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \vsTmp\Local.py
'''

def Get_Local_Data(fn,sta):
    try:
        with open(r'\\10.216.36.222\fcst\ECMWF_POST\STATION\09_FCST\operation\Town\N_SEVP_NMC_RFFC_SFER_EME_AGLB_L88_P9_%s200024012.txt'%(fn),'r',encoding='GB2312') as fin:
            for i in range(4):
                fin.readline()
            sta_num=int(fin.readline())
            sta_tibet={}
            for iSt in range(sta_num):
                result = fin.readline().split()
                sta_tibet[result[0][1:]]=[result[1],result[2],result[3]]
                fin.readline()
                tmp = fin.readline().split()
                sta_tibet[result[0][1:]].append(tmp[11])
                sta_tibet[result[0][1:]].append(tmp[12])
                for i in range(18):
                    fin.readline()
            for xz in list(sta_tibet.keys()):
                if xz in sta:
                    pass
                else:
                    del sta_tibet[xz]
        df = pd.DataFrame(sta_tibet)
        df = pd.DataFrame(df.values.T,index = df.columns,columns = ['lon','lat','hi','tmax','tmin']).reset_index()
        return df
    except FileNotFoundError:
        print("没有找到'N_SEVP_NMC_RFFC_SFER_EME_AGLB_L88_P9_%s200024012.txt'文件"%(fn))
        return

if __name__=='__main__':
    import datetime
    import configparser
    import os
    import pandas as pd 
    CONfIGFILEDIR = os.path.join(os.getcwd(),'config')
    cf = configparser.ConfigParser()
    cf.read(os.path.join(CONfIGFILEDIR,'cimiss.ini'),encoding='UTF-8')
    sta = cf.get('InterfaceParameters','staIds').split(',')
    
    # localtime = datetime.date.today().strftime("%Y%m%d")
    localtime = '20200927'
    print(
        Get_Local_Data(localtime,sta)
    )