'''
import tabula as tb

df = tb.read_pdf('NOC.pdf.pdf', pages='all')[0]
tb.convert_into('NOC.pdf.pdf', 'NOC.csv', output_format='csv', pages='all')
print(df)
'''
from tabula import convert_into
table_file = 'NOC.pdf.pdf'
output_csv = r"noc.csv"
df = convert_into(table_file, output_csv, output_format='csv', lattice=True, stream=False, pages="all")