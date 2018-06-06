# -*- coding: utf-8 -*-

import xlsxwriter
import re


class w2e(object):


    def filter_cold_data(self):

        # with open("../TestData/cold_raw_data.txt", 'r') as file1:
        #     print(re.findall(r'', file1.read()))
        f1 = open("../TestData/cold_raw_data.txt", 'r')
        while True:
            line = f1.readline()
            if not line:
                break
            s1 = re.findall(r'TotalTime: (\w+)*', line, re.M)  #多行匹配

            print(s1)

    def filter_hot_data(self):
        with open("../TestData/hot_raw_data.txt", 'r') as file2:
            print(file2.read())

    def write_data(self):
        # Create an new Excel file and add a worksheet.
        workbook = xlsxwriter.Workbook('../report/TestReport.xlsx')
        worksheet = workbook.add_worksheet()

        # Widen the first column to make the text clearer.
        worksheet.set_column('A:A', 20)

        # Add a bold format to use to highlight cells.
        bold = workbook.add_format({'bold': True, 'font_color': 'red'})

        # Write some simple text.
        worksheet.write('A1', 'Hello')

        # Text with formatting.
        worksheet.write('A2', 'World', bold)

        # Write some numbers, with row/column notation.
        worksheet.write(2, 0, 123)
        worksheet.write(3, 0, 123.456)


        # Insert an image.
        # worksheet.insert_image('B5', 'logo.png')

        workbook.close()


if __name__ == '__main__':
    w2e().filter_cold_data()