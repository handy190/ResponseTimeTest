# -*- coding: utf-8 -*-

import xlsxwriter
from base.Activities import Activities
import datetime

class Data(object):
    """数据处理类，将结果写入excel表格中生成测试报告"""

    def write_data_2_excel(self):
        """
        将数据写入excel
        :return:
        """

        #   获取系统当前时间
        now = datetime.datetime.now()  # 时间数组格式

        #   转换为指定格式时间戳
        timestamp = now.strftime("%H%M%S")

        # Create an new Excel file and add a worksheet.
        workbook = xlsxwriter.Workbook('../report/TestReport' + timestamp+ '.xlsx')
        worksheet = workbook.add_worksheet("测试报告")

        # Widen the first column to make the text clearer.
        worksheet.set_column('A:A', 1)
        worksheet.set_column('B:B', 1)
        worksheet.set_column('C:C', 35)
        worksheet.set_column('D:M', 6)
        worksheet.set_column('O:X', 6)
        worksheet.set_row(1, 30)
        worksheet.set_row(2, 30)
        worksheet.set_row(3, 30)
        worksheet.set_row(4, 30)
        worksheet.set_row(5, 30)
        worksheet.set_row(2, 30)
        worksheet.set_row(8, 40)
        worksheet.set_row(7, 25)

        merge_format = workbook.add_format({
            'bg_color': 'yellow',
            'bold': True,
            'border': 6,
            'align': 'center',
            'valign': 'vcenter'
        })

        merge_format1 = workbook.add_format({
            'bg_color': '#FF8000',
            'bold': True,
            'border': 6,
            'font': '微软雅黑',
            'font_size': 14,
            'align': 'center',
            'valign': 'vcenter'
        })

        # Add a bold format to use to highlight cells.
        cell_format1 = workbook.add_format({
            'bold': True,
            'font_color': 'black',
            'font_size': 12,
            'border': 6,
            'font': 'Arial Unicode MS',
            'bg_color': 'yellow',
            'align': 'center',
            'valign': 'vcenter'
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

        cell_format5 = workbook.add_format({
            'font_size': 12,
            'font': '微软雅黑',
            'border': 6,
            'bg_color': 'FF8000',
            'align': 'center',
            'valign': 'vcenter'
        })

        # 居中对齐
        # cell_format1.set_align('vcenter')
        # cell_format1.set_align('center')

        # ################报告表头部分#####################
        worksheet.merge_range('C2:N2', 'XXX项目性能测试-响应时间测试报告', merge_format1)
        worksheet.merge_range('D3:N3', '', merge_format1)
        worksheet.merge_range('D4:N4', '', merge_format1)
        worksheet.merge_range('D5:N5', '', merge_format1)
        worksheet.merge_range('D6:N6', '', merge_format1)
        worksheet.write('C3', '项目名称', cell_format5)
        worksheet.write('C4', '软件版本', cell_format5)
        worksheet.write('C5', '测试时间', cell_format5)
        worksheet.write('C6', '测试结果', cell_format5)

        # ################数据部分#########################
        worksheet.merge_range('C8:C9', '应用包名', merge_format)
        worksheet.merge_range('D8:N8', '冷启动(单位:ms)', merge_format)
        worksheet.merge_range('O8:Y8', '热启动(单位:ms)', merge_format)
        worksheet.write('D9', '1st', cell_format1)
        worksheet.write('E9', '2nd', cell_format1)
        worksheet.write('F9', '3rd', cell_format1)
        worksheet.write('G9', '4th', cell_format1)
        worksheet.write('H9', '5th', cell_format1)
        worksheet.write('I9', '6th', cell_format1)
        worksheet.write('J9', '7th', cell_format1)
        worksheet.write('K9', '8th', cell_format1)
        worksheet.write('L9', '9th', cell_format1)
        worksheet.write('M9', '10th', cell_format1)
        worksheet.write('N9', 'Average', cell_format1)
        worksheet.write('O9', '1st', cell_format1)
        worksheet.write('P9', '2nd', cell_format1)
        worksheet.write('Q9', '3rd', cell_format1)
        worksheet.write('R9', '4th', cell_format1)
        worksheet.write('S9', '5th', cell_format1)
        worksheet.write('T9', '6th', cell_format1)
        worksheet.write('U9', '7th', cell_format1)
        worksheet.write('V9', '8th', cell_format1)
        worksheet.write('W9', '9th', cell_format1)
        worksheet.write('X9', '10th', cell_format1)
        worksheet.write('Y9', 'Average', cell_format1)
        cell_format2.set_align('vcenter')
        cell_format3.set_align('vcenter')

        # 写入包名
        i = 0
        for appName, activityName in Activities.__members__.items():
            worksheet.write('C'+str(10 + i), str(activityName.value).split('/')[0], cell_format2)
            i += 1

        # 求平均值
        j = 0
        for appName, activityName in Activities.__members__.items():
            worksheet.write_formula('N' + str(10 + j),
                                    '=AVERAGE(D' + str(10 + j) + ':M' + str(10 + j) + ')',
                                    cell_format4)
            worksheet.write_formula('Y' + str(10 + j),
                                    '=AVERAGE(O' + str(10 + j) + ':X' + str(10 + j) + ')',
                                    cell_format4)
            j += 1

        # 写入冷启动数据
        with open("../TestData/cold_raw_data.txt", 'r') as file1:
            lines = file1.readlines()
            column = 0
            row = 0
            for i in lines:
                if 'TotalTime' in i:
                    cold_data = int(i.split(': ')[1])

                    if column > 9:
                        row += 1
                        column = 0
                    worksheet.write_number(9 + row, 3 + column, cold_data, cell_format3)
                    column += 1

        # 写入热启动数据
        with open("../TestData/hot_raw_data.txt", 'r') as file2:
            lines = file2.readlines()
            column = 0
            row = 0
            for i in lines:
                if 'TotalTime' in i:
                    hot_data = int(i.split(': ')[1])

                    if column > 9:
                        row += 1
                        column = 0
                    worksheet.write_number(9 + row, 14 + column, hot_data, cell_format3)
                    column += 1

        workbook.close()
