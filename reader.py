from openpyxl import load_workbook

workbook = load_workbook('users.xlsx')
worksheet = workbook['Лист-1']
for i in worksheet.iter_rows(min_row=2):
    print(i[0].value)
    print(i[1].value)
    print(i[2].value)
    print(i[3].value)
    print(i[4].value)
    print('---------------------')
