'''
Author: Oneice
Date: 2020-12-21 09:58:03
LastEditTime: 2020-12-22 18:49:12
LastEditors: Please set LastEditors
Description: 
FilePath: \vsTmp\SMOC.py
'''
import os
import arrow
import pandas as pd
import configparser
class GetSMOCData():
    """
    docstring
    """
    def __init__(self) :
        self.Year = arrow.now().year
        self.Month = arrow.now().month
        self.Hour = arrow.now().hour
        if self.Hour < 14:
            self.Day = arrow.now().shift(days = -1).day
        else:
            self.Day = arrow.now().day
        self.BasePath ="\\\\10.216.30.39\\DataCenter\\DataService\\SEVP\\RFFC\\SCMOC\\{}\\{}".format(self.Year,arrow.now().replace(day=self.Day).format('YYYYMMDD'))
        with open('./RelatedData/74_sta.txt','r',encoding='gbk') as f:
            self.sta_xz={}
            for i in range(74):
                id,name=f.readline().split()
                self.sta_xz[id]=[name]
    
    def FilePath(self):
        path = self.BasePath
        for root,dirs,files in os.walk(path):
            for file in files:
                now_date = arrow.now().format('YYYYMMDD')
                if now_date in file:
                    return path+"\\"+file
    
    def ReadFiles(self):
        path = GetSMOCData.FilePath(self)
        with open (path,'r') as f:
            for i in range(4): f.readline() 
            totalNum=int(f.readline())
            staTotal={}                             
            for iSt in range(totalNum):
                result = f.readline().split()
                id=result[0]
                lon=result[1]
                lat=result[2]
                hi=result[3]
                row=result[4]
                cco=result[5]
                for j in range(7): f.readline()
                tmp=f.readline().split()
                for j in range(20): f.readline()
                staTotal[id]=[lon,lat,hi,tmp[11],tmp[12]]
        for xz in list(staTotal.keys()):
            sta_xzList = self.sta_xz.keys()
            if xz in sta_xzList:
                pass
            else:
                del staTotal[xz]
        df = pd.DataFrame(staTotal)
        df = pd.DataFrame(df.values.T,index = df.columns,columns = ['lon','lat','hi','tmax','tmin']).reset_index()
        return df
if __name__ == "__main__":
    smoc = GetSMOCData()
    # result = smoc.FilePath()
    # print(result)
    a = smoc.ReadFiles()
    print(a)
    print(type(a))
    pd.set_option('colheader_justify', 'center')   # FOR TABLE <th>
    html_string = '''
    <html>
    <head><title>温度差异展示</title></head>
    <link rel="stylesheet" type="text/css" href="RelatedData/df_style.css"/>
    <h1>温度差异展示</h1>
    <center>
    <div class= "container">
    <div class="left"><h2>aaa</h2><marquee direction="up">{table}</marquee></div>
    <div class="middle"><h2>aaa</h2>{table}</div>
    <div class="right"><h2>aaa</h2>{table}</div>
    </div>
    </center>
    </html>
    '''
    # OUTPUT AN HTML FILE
    with open('myhtml.html', 'w') as f:
        f.write(html_string.format(table=a.to_html(classes='mystyle')))