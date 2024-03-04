from pdf2image import convert_from_path, convert_from_bytes
import os
import time
import logging
DATE_FORMAT = '%m/%d/%Y %H:%M:%S %p'
LOG_FORMAT = ''
logging.basicConfig(
    filename='ddpm.log', 
    # filemode=
    )

cwd = './pdfimg'
if not os.path.exists(cwd):
    os.makedirs(cwd)
    print(time.strftime('%m/%d/%Y - %H:%M:%S ', time.localtime()), end='')
    print(f'创建文件夹{cwd}')

images = convert_from_path('./tex/ddpm.pdf', output_file='./')

for idx,image in enumerate(images):
    image.save(fr'./pdfimg/{idx}.png')
