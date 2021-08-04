from python_files.utils import *
from python_files import import_data

path_file = "input_files/file 062021.xls"
data_captured = import_data.import_from_xls(path_file)
file1_output = open('output_files/Vendas por Produto.csv', 'w') # Create a new CSV File for Sale per Product
file2_output = open('output_files/Info Pagamentos por Venda.csv', 'w') # Create a new CSV File for Payments Info per Sale

all_payments = data_captured[0]
all_sales = data_captured[1]

for _ in all_sales:
    
    line = f"{_[0]};{_[1]};{_[2]};{_[3]};{_[4]};{_[5]};{brazil_currency_notation(_[6])};\
        {brazil_currency_notation(_[7])};{brazil_currency_notation(_[8])};\
        {brazil_currency_notation(_[9])};{brazil_currency_notation(_[10])}\n"
    file1_output.write(line)

for _ in all_payments:
    
    line = f"{_[0]};{_[1]};{_[2]};{_[3]};{brazil_currency_notation(_[4])}\n"
    file2_output.write(line)

file1_output.close()
file2_output.close()