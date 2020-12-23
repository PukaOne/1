'''
Author: your name
Date: 2020-12-21 18:55:13
LastEditTime: 2020-12-23 11:59:27
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \vsTmp\CIMISS.py
'''
import os
import json
import requests
import datetime as dt
import pandas as pd
import configparser

CONfIGFILEDIR = os.path.join(os.getcwd(),'config')
cf = configparser.ConfigParser()
cf.read(os.path.join(CONfIGFILEDIR,'cimiss.ini'),encoding='UTF-8')


class CimissData():
    def __init__(self)->None:
        self.http = f'http://{cf.get("CIMISS", "DNS")}/cimiss-web/api?'
        self.userId = cf.get('CIMISS', 'USER_ID')
        self.pwd = cf.get('CIMISS', 'PASSWORD')
    def get_tem(self, start_date, end_date)->pd.DataFrame:
        interfaceId = cf.get('InterfaceParameters', 'interfaceId')
        dataCode = cf.get('InterfaceParameters', 'dataCode')
        elements = cf.get('InterfaceParameters', 'elements')
        staIds = cf.get('InterfaceParameters','staIds')
        dataFormat = cf.get('InterfaceParameters' , 'dataFormat')

        timeRange = f'[{int(start_date)},{int(end_date)}]'
        url = f'''{self.http}userId={self.userId}&pwd={self.pwd}&interfaceId={interfaceId}&dataCode={dataCode}&elements={elements}&timeRange={timeRange}&staIds={staIds}&dataFormat={dataFormat}'''
        
        data = requests.get(url).text
        dict_data = json.loads(data)
        df = pd.DataFrame(dict_data['DS'][-74:])
        return df

if __name__ == '__main__':
    start_time = pd.Timestamp('20200926000000').strftime('%Y%m%d%H%M%S')
    end_time = pd.Timestamp('20200926060000').strftime('%Y%m%d%H%M%S')
    print(type(start_time))
    cm = CimissData()
    c = cm.get_tem(start_time,end_time)
    print(c)