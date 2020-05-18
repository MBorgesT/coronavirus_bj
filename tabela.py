import xlrd

loc = ('corona_bji.xlsx')
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)