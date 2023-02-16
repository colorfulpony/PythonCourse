import dnb
import sunbiz
import gspread
import string


# Validate String Punctuation
def string_punctuation(s):
    whitelist = string.ascii_letters + string.digits + ' ' + "&" + "'" + "-"
    for char in string.punctuation:
        if char not in whitelist:
            s = s.replace(char, '')
    return s


# Connection To Worksheet
gc = gspread.service_account('secrets.json')
spreadsheet = gc.open('Copy of Landscaper - FL')
worksheet = spreadsheet.worksheet('HUB_20230205_(808)')

# Start in Sheet
cell_row = 2

whileloop = True
while whileloop:
    try:
        # Cells Id
        company_name_cell_id = f'A{cell_row}'
        full_name_cell_id = f'B{cell_row}'
        first_name_cell_id = f'C{cell_row}'
        last_name_cell_id = f'D{cell_row}'

        # Company Name
        company_name = string_punctuation(worksheet.acell(company_name_cell_id).value.upper())

        # Get Full Name, First Name, Last Name of Owner by sunbiz
        result_sunbiz = sunbiz.get_company_owner_by_sunbiz(company_name)

        # Update Worksheet
        if result_sunbiz is None:
            # Get Full Name, First Name, Last Name of Owner by dnb
            result_dnb = dnb.get_company_owner_by_bnd(company_name)
            if result_dnb is not None and result_dnb is not False:
                worksheet.update(full_name_cell_id, result_dnb[0])
                worksheet.update(first_name_cell_id, result_dnb[1])
                worksheet.update(last_name_cell_id, result_dnb[2])
            elif result_dnb is False:
                print("Something went wrong with dnb")
            elif result_dnb is None:
                print('dnb has not such company')
                worksheet.update(full_name_cell_id, '-')
                worksheet.update(first_name_cell_id, '-')
                worksheet.update(last_name_cell_id, '-')

        elif result_sunbiz is not None and result_sunbiz is not False:
            worksheet.update(full_name_cell_id, result_sunbiz[0])
            worksheet.update(first_name_cell_id, result_sunbiz[1])
            worksheet.update(last_name_cell_id, result_sunbiz[2])
        elif result_sunbiz is False:
            print("Something went wrong with sunbiz")
        elif result_sunbiz is None:
            print('sunbiz has not such company')
            worksheet.update(full_name_cell_id, '-')
            worksheet.update(first_name_cell_id, '-')
            worksheet.update(last_name_cell_id, '-')
    except Exception as ex:
        print(ex)

    # Update cell row
    cell_row += 1
