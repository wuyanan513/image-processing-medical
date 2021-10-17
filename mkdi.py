import xlrd
import os

def xls_read(xls_path):
    folder_name=[]
    read_book=xlrd.open_workbook(xls_path)
    table=read_book.sheet_by_index(1)
    nrows=table.nrows
    # read value and save
    for i in range(1,nrows):
        folder_name.append(table.cell_value(i,0))
    return  folder_name

if __name__ == '__main__':
    xls_path='I:/ratio.xls'
    save_path='I:/data_3_ct'
    name = xls_read(xls_path)
    for i in range(len(name)):
        save_images_path=os.path.join(save_path,name[i])
        if not os.path.exists(save_images_path):
            os.makedirs(save_images_path)