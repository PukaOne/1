'''
Author: your name
Date: 2020-12-23 11:02:49
LastEditTime: 2020-12-23 17:52:02
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \vsTmp\mian.py
'''
import CIMISS
import Local
import SMOC
import arrow
import os
import configparser
CONfIGFILEDIR = os.path.join(os.getcwd(),'config')
cf = configparser.ConfigParser()
cf.read(os.path.join(CONfIGFILEDIR,'cimiss.ini'),encoding='UTF-8')
class Exhibition:
    def __init__(self):
        self.nowDate = arrow.now() .format('YYYYMMDDHHmmss')
        self.staIds = cf.get('InterfaceParameters','staIds')
        self.utcnow = arrow.utcnow().replace(minute=0,second=0).format('YYYYMMDDHHmmss')
        self.utcnow_24 = arrow.utcnow().replace(minute=0,second=0).format('YYYYMMDDHHmmss')
        self.dfcimiss = CIMISS.CimissData().get_tem(self.utcnow_24,self.utcnow)
        self.dflocal = Local.Get_Local_Data(self.nowDate,self.staIds)
        # self.dfsmoc = SMOC.GetSMOCData.ReadFiles(self.nowDate,self.staIds)
if __name__ == "__main__":
    demo = Exhibition()ssss
    