from python_files.utils import do_nothing
from xlrd import open_workbook

def general_sales_info(row):
    """
    Find the pivot in the XLS file cells to start capturing general sales information.
    """
    if row[5].find(":") == 2:
        return True
    elif row[0] == "" and row[17] != "":
        return True
    elif row[0] == "Item":
        return False
    return False

def individual_sales_start(row):
    """
    Find the pivot data in the XLS file cells to START capturing individual information for each item sold.
    """
    if row[0] == "Item":
        return True
    return False

def individual_sales_stop(row):
    """
    Find the pivot data in the XLS file cells to STOP capturing individual information for each item sold.
    """
    if row[1] == "Totais":
        return True
    return False

def import_from_xls(path_file):
    """
    This function was created as an option to capture data directly from Excel file (XLS only).
    """

    workbook = open_workbook(path_file) # OPEN THE FILE
    worksheet = workbook.sheet_by_index(0) # READ THE FIRST SHEET
    rows = worksheet.nrows # RETURN THE MAXIMUM ACTIVE / WRITED ROWS

    global emission, hour, document, flag
    flag = False
    all_payments = []
    all_sales = []
    
    try:
        counter = 0
        while counter <= rows: # Percorre todo o arquivo na sheet selecionada enquanto houver linha preenchidas

            # LINE BELOW: Read line by line from the XLS file (May not work with XLSX file)
            row = worksheet.row_values(counter, start_colx=0, end_colx=None)
            #input(row) #DEBBUG

            if general_sales_info(row):
                if row[4] != "":
                    emission = row[4]
                    hour = row[5]
                    document = row[6]
                else:
                    pass
                payment = row[17]
                payment_value = row[18]
                local_payments = (emission, hour, document, payment, payment_value)
                all_payments.append(local_payments)
                #input(f"\n>> {counter+1}  {all_payments}") # DEBBUG
            
            elif individual_sales_start(row):
                flag = True

            elif individual_sales_stop(row):
                flag = False

            elif flag is True:
                item_code = row[1]
                item_description = row[2]
                item_type = row[3]
                item_quantity = row[6]
                item_price = row[7]
                item_descount = row[8]
                item_addition = row[9]
                item_final_value = row[10]
                local_sale = (item_code, item_description, item_type, emission, hour, document,\
                    item_quantity, item_price, item_descount, item_addition, item_final_value) # This left pipeline is just a line breaker
                all_sales.append(local_sale)
                #print(f"\n>> {counter}  {all_sales}") # DEBBUG
            
            counter += 1

    except:
        do_nothing
    
    return [all_payments, all_sales]

# These two lines should be uncommented only in case you want to use only this module for debugging
#path_file = "arquivo.xls" # Inform the file path
#import_from_xls(path_file)