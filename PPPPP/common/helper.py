import xlrd,logging,os


 # 打印用例路径
class Helper(object):
    def readExcles(self,rowx):
        #rowx是行数
        #：param rowx：
        # return：返回的每一行的行数

        book = xlrd.open_workbook(r'D:\pythonProject\PPPPP\data\info.xls', 'r')
        table = book.sheet_by_index(0)
        return table.row_values(rowx)

    def readusername(self,rowx):   #定义第一列
        return str(self.readExcles(rowx)[2])

    def readpassword(self,rowx):
        return str(self.readExcles(rowx)[3])

    def exceptText(self,rowx):
        return str(self.readExcles(rowx)[6])

    def dirname(self,filename,filepath='data'):
        return os.path.join(os.path.dirname(os.path.dirname(__file__)),filepath,filename)

