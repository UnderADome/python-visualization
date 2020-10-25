#encoding:utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import xlwt
from prettytable import PrettyTable
from PIL import Image, ImageDraw, ImageFont
import sys
import os

def crawl():
    #打开网页
    html = urlopen("http://data.hb.stats.cn/CityData.aspx?DataType=65&ReportType=1")
    bsObj = BeautifulSoup(html.read(), "lxml")
    
    titles = []
    for title in bsObj.find("tr", {"class":"tr-title"}).find_all("td"):
        titles.append(title.getText())
    # datas = []
    # for data in bsObj.find("tr", {"class":"tr-title"}).find("")
    print (titles)


    datas = []
    dd = []
    for data in bsObj.find_all("tr", {"class":"tr-title"}):
        for d in data.find_all("td"):
            dd.append(d.getText())
        datas.append(dd)
        dd = []    
    #print (datas)
    return datas

def set_style(name, height, bold = False):
    style = xlwt.XFStyle() #初始化样式
    font = xlwt.Font() #为样式创建字体
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style

def write_excel():
    #创建工作簿
    workbook = xlwt.Workbook(encoding="utf-8")
    #创建sheet
    data_sheet = workbook.add_sheet("show_data")

    datas = crawl()

    index = 0
    for i in datas:
        for x, item in enumerate(i):
            data_sheet.write(index, x, item, set_style('Times New Roman',220, True))
        index += 1

    workbook.save("data.xls")

def draw_puc():
    datas = crawl()

    tab = PrettyTable()
    #设置表头
    #tab.field_names = []
    index = 0
    #表格内容
    for data in datas:
        tab.add_row(data)
        index += 1

    print(tab.encoding)
    #print (tab)
    tab_info = tab.get_string()
    #print(tab_info)



    space = 15
    #PIL模块中，确定写入到图片中的文本字体
    #font = ImageFont.truetype('/Library/Fonts/华文细黑.ttf', 20)
    #Image模块创建一个图片对象
    im = Image.new('RGB', (10, 10), (0, 0, 0, 0))
    #ImageDraw向图片中进行操作，写入文字后者插入线条都可以
    draw = ImageDraw.Draw(im, "RGB")
    
    #根据插入图片中的文字内容和字体信息，来确定的那个图片的最终大小
    img_size = draw.textsize(tab_info)
    #图片初始化的大小为10-10，现在根据图片内容要重新设置图片的大小
    im_new = im.resize((img_size[0]+space*2, img_size[1]+space*2))
    draw = ImageDraw.Draw(im_new, "RGB")
    #批量写入到图片中，这里的multiline_Text会自动识别换行符
    draw.text((space, space), tab_info, fill=(255,255,255))
    
    #im_new.save('12345.PNG', "PNG")
    im_new.show()

if __name__ == '__main__':
    print (sys.getdefaultencoding())
    
    #write_excel()
    print("创建你xlsx文件成功")
    draw_puc()
    print("绘图完毕")
    
