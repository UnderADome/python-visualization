import xlrd
import matplotlib.pyplot as plt
import numpy as np
import os

def read_excel():
    print(os.getcwd())
    #打开excel文件
    workbook = xlrd.open_workbook('data.xlsx')
    #workbook = xlrd.open_workbook(os.path.join(os.getcwd(), 'data.xlsx'))
    #打开sheet1
    sheet = workbook.sheet_by_name("Sheet1")
    #获取行数
    row_num = sheet.nrows
    row_list = []
    for i in range(1, row_num):
        #获得第i行的数据
        row_data = sheet.row_values(i)
        for data in row_data:
            if data != '':
                row_list.append(data)
    # for row in row_list:
    #     print (row)

    return sorted(row_list)

def draw_picture(row_list):
    
    plt.ylabel("speed of Pedestrians 行人速度", fontproperties='SimHei')
    plt.bar(range(len(row_list)), row_list)
    #平均数
    print("平均数：", np.mean(row_list))
    print("平均数：" + str(np.mean(row_list)))
    #中位数
    print("中位数：", np.median(row_list))
    plt.show()

if __name__ == '__main__':
    draw_picture(read_excel())