import os
import pdfkit
from os import listdir
from os.path import isfile, join

# os.chdir(r'D:\Users\kuzmichev\Desktop\Ann\cards')

folder = r'D:\Users\kuzmichev\Desktop\Ann\cards'

config_path = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
# pdfkit.from_file(r'D:\Users\kuzmichev\Desktop\Ann\cards\Атос_id_15.html', 
#                  r'D:\Users\kuzmichev\Desktop\Ann\cards\Атос_id_15.pdf' , 
#                  configuration=config_path, 
#                  options={"enable-local-file-access": ""} )


cards = [f for f in listdir(folder) if isfile(join(folder, f))]

for card in cards:
    print(card)
    inName = folder +'\\' + card
    outName = folder + '\\pdf\\' + card.split('.')[0] + '.pdf'
    print('inName', inName)
    print('outName', outName)
    # config_path = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    pdfkit.from_file(inName, 
                    outName, 
                    configuration=config_path,
                    options={"enable-local-file-access": ""} )

    # pdfkit.from_file(r'D:\Users\kuzmichev\Desktop\Ann\cards\Арамис_id_14.html', r'D:\Users\kuzmichev\Desktop\Ann\cards\Арамис_id_14.pdf' , configuration=config_path)
# pdfkit.from_string('Hello!', 'out2.pdf')
