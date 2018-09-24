
import xlrd
import os

excelPath = os.path.dirname(__file__) + r'\data.xlsx'
sheetName = 'Sheet1'


class ExcelUtil(object):

    def __init__(self):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)

        # 获取title
        self.row = self.table.row_values(0)

        # 获取行数
        self.rowNum = self.table.nrows

        # 获取列数
        self.colNum = self.table.ncols

        # 过滤第一行数据，从第二行开始
        self.curRowNo = 1

    def getAllParams(self, tag):
        allParams = []
        while self.hasNext():
            rowParam = {}
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                rowParam[self.row[x]] = col[x]
            if rowParam['tag'] == tag:
                allParams.append(rowParam)
            self.curRowNo += 1
        return allParams

    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True
