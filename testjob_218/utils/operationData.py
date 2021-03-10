import os
import xlrd

class OperationData(object):
    def dir_base(self,fileName,filePath='data'):
        return os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))),filePath,fileName)


    def getData(self,sheet_name):
        rows=[]
        book=xlrd.open_workbook(self.dir_base('caseManage.xlsx'),'r')
        sheet=book.sheet_by_name(sheet_name)
        for row in range(1,sheet.nrows):
            rows.append(sheet.row_values(row,1,sheet.ncols))

        return rows

