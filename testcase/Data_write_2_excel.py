# -*- coding: utf-8 -*-

import xlsxwriter

"""
数据处理类，将结果写入excel表格中生成测试报告
"""
class Data(object):

    def filter_cold_data(self):

        with open("../TestData/cold_raw_data.txt", 'r') as file1:
            lines = file1.readlines()
            for i in lines:
                if 'TotalTime' in i:
                    cold_data = str(i.split(': ')[1])  # 注意split(': ')后面有个空格

    def filter_hot_data(self):
        with open("../TestData/hot_raw_data.txt", 'r') as file2:
            lines = file2.readlines()
            for i in lines:
                if 'TotalTime' in i:
                    hot_data = str(i.split(': ')[1])

    def write_data_2_excel(self):
        # Create an new Excel file and add a worksheet.
        workbook = xlsxwriter.Workbook('../report/TestReport.xlsx')
        worksheet = workbook.add_worksheet()


        # Widen the first column to make the text clearer.
        worksheet.set_column('A:A', 20)

        # Add a bold format to use to highlight cells.
        cell_format = workbook.add_format({'bold': True, 'font_color': 'red'})

        # Write some simple text.
        worksheet.write('A1', 'Hello')

        # Text with formatting.
        worksheet.write('A2', 'World', cell_format)

        # Write some numbers, with row/column notation.
        cell_format.set_font_color('green')
        worksheet.write(2, 0, 123)
        worksheet.write(3, 0, 123.456)


        # Insert an image.
        # worksheet.insert_image('B5', 'logo.png')

        workbook.close()


if __name__ == '__main__':
    Data().filter_cold_data()