# -*- coding: utf-8 -*-

import xlsxwriter
from base.Activities import Activities

"""
数据处理类，将结果写入excel表格中生成测试报告
"""
class Data(object):


    def write_data_2_excel(self):
        """
        将数据写入excel
        :return:
        """

        # Create an new Excel file and add a worksheet.
        workbook = xlsxwriter.Workbook('../report/TestReport.xlsx')
        worksheet = workbook.add_worksheet('TestData')

        # Widen the first column to make the text clearer.
        worksheet.set_column('C:C', 35)
        worksheet.set_row(2, 40)
        worksheet.set_row(1, 25)

        merge_format = workbook.add_format({
            'bg_color': 'yellow',
            'bold': True,
            'border': 6,
            'align': 'center',
            'valign': 'vcenter',
        })


        # Add a bold format to use to highlight cells.

        cell_format1 = workbook.add_format({
            'bold': True,
            'font_color': 'black',
            'font_size': 12,
            'border': 6,
            'font': 'Arial Unicode MS',
            'bg_color': 'yellow'
        })

        # 包名格式
        cell_format2 = workbook.add_format({
            'font_size': 11,
            'font': 'Meiryo',
            'border': 6
        })

        # 数据格式
        cell_format3 = workbook.add_format({
            'font_size': 11,
            'font': 'Arial Narrow',
            'border': 6
        })

        # 平均值格式
        cell_format4 = workbook.add_format({
            'font_size': 12,
            'font': 'Arial Black',
            'border': 6
        })

        # 居中对齐
        cell_format1.set_align('vcenter')
        cell_format1.set_align('center')

        worksheet.merge_range('C2:C3', '包名', merge_format)
        worksheet.merge_range('D2:N2', '冷启动', merge_format)
        worksheet.merge_range('O2:Y2', '热启动', merge_format)
        worksheet.write('D3', '1st', cell_format1)
        worksheet.write('E3', '2nd', cell_format1)
        worksheet.write('F3', '3rd', cell_format1)
        worksheet.write('G3', '4th', cell_format1)
        worksheet.write('H3', '5th', cell_format1)
        worksheet.write('I3', '6th', cell_format1)
        worksheet.write('J3', '7th', cell_format1)
        worksheet.write('K3', '8th', cell_format1)
        worksheet.write('L3', '9th', cell_format1)
        worksheet.write('M3', '10th', cell_format1)
        worksheet.write('N3', 'Average', cell_format1)
        worksheet.write('O3', '1st', cell_format1)
        worksheet.write('P3', '2nd', cell_format1)
        worksheet.write('Q3', '3rd', cell_format1)
        worksheet.write('R3', '4th', cell_format1)
        worksheet.write('S3', '5th', cell_format1)
        worksheet.write('T3', '6th', cell_format1)
        worksheet.write('U3', '7th', cell_format1)
        worksheet.write('V3', '8th', cell_format1)
        worksheet.write('W3', '9th', cell_format1)
        worksheet.write('X3', '10th', cell_format1)
        worksheet.write('Y3', 'Average', cell_format1)
        cell_format2.set_align('vcenter')
        cell_format3.set_align('vcenter')

        # 写入包名
        i = 0
        for appName, activityName in Activities.__members__.items():
            worksheet.write('C'+str(4 + i), str(activityName.value).split('/')[0], cell_format2)
            i = i + 1
        # 求平均值
        j = 0
        for appName, activityName in Activities.__members__.items():
            worksheet.write_formula('N' + str(4 + j), '=AVERAGE(D' + str(4 + j) + ':M' + str(4 + j) + ')', cell_format4)
            worksheet.write_formula('Y' + str(4 + j), '=AVERAGE(O' + str(4 + j) + ':X' + str(4 + j) + ')', cell_format4)
            j = j + 1

        # 写入冷启动数据
        with open("../TestData/cold_raw_data.txt", 'r') as file1:
            lines = file1.readlines()
            column = 0
            row = 0
            for i in lines:
                if 'TotalTime' in i:
                    cold_data = int(i.split(': ')[1])

                    if column > 9:
                        row = row + 1
                        column = 0
                    worksheet.write_number(3 + row, 3 + column, cold_data, cell_format3)
                    column = column + 1


        # 写入热启动数据
        with open("../TestData/hot_raw_data.txt", 'r') as file2:
            lines = file2.readlines()
            column = 0
            row = 0
            for i in lines:
                if 'TotalTime' in i:
                    hot_data = int(i.split(': ')[1])

                    if column > 9:
                        row = row + 1
                        column = 0
                    worksheet.write_number(3 + row, 14 + column, hot_data, cell_format3)
                    column = column + 1

        workbook.close()
