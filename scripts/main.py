import pandas as pd
import os
class Solution:
    def __init__(self):
        self.file=0
    def create_sheet(self, name):

        sh=pd.ExcelWriter('../data/data_sheet_'+name+'.xlsx', engine='xlsxwriter')
        self.file = sh;
        self.file.save()


p=Solution()
p.create_sheet('d')
p.add_df({'Name': ['A', 'B', 'C', 'D'],'Age': [10, 0, 30, 50]})

