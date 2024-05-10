from openpyxl import load_workbook


workbook = load_workbook('profile.xlsx')


def get_contact_info():
    worksheet = workbook['contact_info']
    for row in worksheet.iter_rows(min_row=2, values_only=True):
        data = {
            'fullname': row[0],
            'phone': row[1],
            'email': row[2],
            'linkedin': row[3],
            'location': row[4],
            'about_me': row[5]
        }
        print(data)
        return data


def get_education():
    worksheet = workbook['education']

    for row in worksheet.iter_rows(min_row=2, values_only=True):
