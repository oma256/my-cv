import xlsxwriter

workbook = xlsxwriter.Workbook('users.xlsx')
worksheet = workbook.add_worksheet('Лист-1')

bold = workbook.add_format({'bold': True})
bold_center = workbook.add_format({'bold': True, 'align': 'center'})
center = workbook.add_format({'align': 'center'})

worksheet.set_column('A1:A1', 3)
worksheet.set_column('B1:B1', 30)
worksheet.set_column('C1:C1', 25)
worksheet.set_column('D1:D1', 15)
worksheet.set_column('E1:E1', 10)

worksheet.write('A1', '№', bold_center)
worksheet.write('B1', 'ФИО', bold_center)
worksheet.write('C1', 'Почта', bold_center)
worksheet.write('D1', 'Номер телефона', bold_center)
worksheet.write('E1', 'ЗП', bold_center)


users_list = [
    {
        'number': 123, 
        'fullname': 'Omurbek Dulatov', 
        'email': 'oma.dulatov@gmail.com',
        'phone_number': '+996555453445',
        'sallary': 45000
    },
    {
        'number': 124, 
        'fullname': 'Asanov Emil', 
        'email': 'asanov.emil@gmail.com',
        'phone_number': '+996555467445',
        'sallary': 125000
    },
    {
        'number': 125, 
        'fullname': 'Sam Smith', 
        'email': 'sam.smith@gmail.com',
        'phone_number': '+996555453785',
        'sallary': 45000
    },
    {
        'number': 126, 
        'fullname': 'Omurbek Dulatov', 
        'email': 'oma.dulatov@gmail.com',
        'phone_number': '+996555455645',
        'sallary': 55000
    },
    {
        'number': 127, 
        'fullname': 'Omurbek Dulatov', 
        'email': 'oma.dulatov@gmail.com',
        'phone_number': '+996555455645',
        'sallary': 95000
    }
]

amount = 0
last_row = 1

for index, user in enumerate(users_list, start=1):
    worksheet.write(index, 0, user['number'])
    worksheet.write(index, 1, user['fullname'])
    worksheet.write(index, 2, user['email'])
    worksheet.write(index, 3, user['phone_number'], center)
    worksheet.write(index, 4, user['sallary'])

    amount += user['sallary']
    last_row += 1

worksheet.write(last_row, 0, 'Итого:', bold_center)
worksheet.write(last_row, 4, amount, bold_center)

workbook.close()
