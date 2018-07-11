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

        cold_difference_value = 500  # 判断标准值与平均值的差值，可根据实际情况改动
        hot_difference_value = 100  # 判断标准值与平均值的差值，可根据实际情况改动

        #   获取系统当前时间
        now = datetime.datetime.now()  # 时间数组格式

        #   转换为指定格式时间戳
        timestamp = now.strftime("%H%M%S")

        # Create an new Excel file and add a worksheet.
        workbook = xlsxwriter.Workbook('../report/PerformanceTestReport' + timestamp+ '.xlsx')
        worksheet = workbook.add_worksheet('测试报告')

        # Widen the first column to make the text clearer.
        worksheet.set_column('A:A', 1)
        worksheet.set_column('B:B', 1)
        worksheet.set_column('C:C', 35)
        worksheet.set_column('D:Q', 8)
        worksheet.set_column('R:AE', 8)
        worksheet.set_row(1, 30)
        worksheet.set_row(2, 30)
        worksheet.set_row(3, 30)
        worksheet.set_row(4, 30)
        worksheet.set_row(5, 30)
        worksheet.set_row(6, 15)
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
            'font_size': 12,
            'font': 'Arial Narrow',
            'border': 6
        })

        # 平均值格式
        cell_format4 = workbook.add_format({
            'font_size': 12,
            'font': 'Arial Black',
            'border': 6
        })

        # 差值格式
        cell_format8 = workbook.add_format({
            'font_size': 12,
            'font': 'Arial Black',
            'border': 6,
            'font_color': 'red'
        })

        # 结果值的格式
        cell_format9 = workbook.add_format({
            'font_size': 12,
            'font': 'Arial Black',
            'border': 6,
            'align': 'center',
            'valign': 'vcenter'
        })

        # 项目描述栏的格式
        cell_format5 = workbook.add_format({
            'font_size': 12,
            'font': '微软雅黑',
            'border': 6,
            'bg_color': 'FF8000',
            'align': 'center',
            'valign': 'vcenter'
        })

        red_format = workbook.add_format({'bg_color': 'red'})

        green_format = workbook.add_format( {'bg_color':  '#BCF57D'})

        # ################报告表头部分#####################
        worksheet.merge_range('C2:Q2', 'XXX项目性能测试-响应时间测试报告', merge_format1)
        worksheet.merge_range('D3:Q3', '', merge_format1)
        worksheet.merge_range('D4:Q4', '', merge_format1)
        worksheet.merge_range('D5:Q5', '', merge_format1)
        worksheet.merge_range('D6:Q6', '', merge_format1)
        worksheet.write('C3', '项目名称', cell_format5)
        worksheet.write('C4', '软件版本', cell_format5)
        worksheet.write('C5', '测试时间', cell_format5)
        worksheet.write('C6', '测试结果', cell_format5)

        # ################数据部分#########################
        worksheet.merge_range('C8:C9', '应用包名', merge_format)
        worksheet.merge_range('D8:Q8', '冷启动(单位:ms)    判断标准: ' + str(cold_difference_value) + 'ms(差值大于该值视为 fail,反之则 pass)', merge_format)
        worksheet.merge_range('R8:AE8', '热启动(单位:ms)    判断标准: ' + str(hot_difference_value) +'ms(差值大于该值视为 fail,反之则 pass)', merge_format)
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
        worksheet.write('O9', '标准值', cell_format1)
        worksheet.write('P9', '差值', cell_format1)
        worksheet.write('Q9', '结果', cell_format1)
        worksheet.write('R9', '1st', cell_format1)
        worksheet.write('S9', '2nd', cell_format1)
        worksheet.write('T9', '3rd', cell_format1)
        worksheet.write('U9', '4th', cell_format1)
        worksheet.write('V9', '5th', cell_format1)
        worksheet.write('W9', '6th', cell_format1)
        worksheet.write('X9', '7th', cell_format1)
        worksheet.write('Y9', '8th', cell_format1)
        worksheet.write('Z9', '9th', cell_format1)
        worksheet.write('AA9', '10th', cell_format1)
        worksheet.write('AB9', 'Average', cell_format1)
        worksheet.write('AC9', '标准值', cell_format1)
        worksheet.write('AD9', '差值', cell_format1)
        worksheet.write('AE9', '结果', cell_format1)
        cell_format2.set_align('vcenter')
        cell_format3.set_align('vcenter')

        # 写入包名
        i = 0
        for appName, activityName in Activities.__members__.items():
            worksheet.write('C'+str(10 + i), str(activityName.value).split('/')[0], cell_format2)
            i += 1

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
                    worksheet.write_number(9 + row, 17 + column, hot_data, cell_format3)
                    column += 1

        # 写入标准值
        cold_standard_values = [1,2,3,4,5,
                                6,7,8,9,10,
                                11,12,13,14,15,
                                16,17,18,19,20,
                                21,22,23]
        hot_standard_values = [1,2,3,4,5,
                               6,7,8,9,10,
                               11,12,13,14,15,
                               16,17,18,19,20,
                               21,22,23]

        for k in range(Activities.__members__.items().__len__()):
            worksheet.write_number('O' + str(10 + k),cold_standard_values[k], cell_format4)
            worksheet.write_number('AC' + str(10 + k), hot_standard_values[k], cell_format4)


        # 求平均值、差值、结果
        for j in range(Activities.__members__.items().__len__()):
            worksheet.write_formula('N' + str(10 + j),
                                    '=AVERAGE(D' + str(10 + j) + ':M' + str(10 + j) + ')',
                                    cell_format4)
            worksheet.write_formula('AB' + str(10 + j),
                                    '=AVERAGE(R' + str(10 + j) + ':AA' + str(10 + j) + ')',
                                    cell_format4)
            worksheet.write_formula('P' + str(10 + j), '=N' + str(10 + j) + '-O' + str(10 + j), cell_format8)
            worksheet.write_formula('AD' + str(10 + j), '=AB' + str(10 + j) + '-AC' + str(10 + j), cell_format8)

            worksheet.write_formula('Q' + str(10 + j), '=IF(P' + str(10 + j) + '>' + str(cold_difference_value) +
                                    ', "Fail", "Pass")',
                                    cell_format9)
            worksheet.write_formula('AE' + str(10 + j), '=IF(AD' + str(10 + j) + '>' + str(hot_difference_value) +
                                    ', "Fail", "Pass")',
                                    cell_format9)

            worksheet.conditional_format('Q10:' + 'Q' + str(10 + j), {'type':      'text',
                                                                       'criteria':  'begins with',
                                                                       'value':     'Fa',
                                                                       'format':    red_format
                                                                       })
            worksheet.conditional_format('Q10:' + 'Q' + str(10 + j), {'type': 'text',
                                                                      'criteria': 'begins with',
                                                                      'value': 'Pa',
                                                                      'format': green_format
                                                                      })


            worksheet.conditional_format('AE10:' + 'AE' + str(10 + j), {'type': 'text',
                                                                      'criteria': 'begins with',
                                                                      'value': 'Fa',
                                                                      'format': red_format
                                                                      })
            worksheet.conditional_format('AE10:' + 'AE' + str(10 + j), {'type': 'text',
                                                                        'criteria': 'begins with',
                                                                        'value': 'Pa',
                                                                        'format': green_format
                                                                        })
        # 缩放80%比例
        worksheet.set_zoom(80)

        # 添加图表
        num = Activities.__members__.items().__len__()
        chart = workbook.add_chart({'type': 'column'})
        chart.add_series({
            'categories': '=测试报告!$C$10:$C$' + str(num + 9),
            'name': '冷启动',
            'values':     '=测试报告!$N$10:$N$' + str(num + 9),
            'gap':        200
        })
        chart.add_series({
            'name': '热启动',
            'values': '=测试报告!$AB$10:$AB$' + str(num + 9),
            'gap': 200
        })

        chart.set_x_axis({
            'name': '应用包名',
            'name_font': {'size': 14, 'bold': True}
        })
        chart.set_y_axis({
            'name': '响应时间/ms',
            'name_font': {'size': 14, 'bold': True}
        })

        chart.set_style(10)

        chart.set_title({
            'name': '响应时间柱状图',
            'overlay': True,
            'layout': {
                'x': 0.42,
                'y': 0.10,
            }
        })
        chart.set_size({'width': 2000, 'height': 800})
        chart.set_plotarea({
            'border': {'color': 'red', 'width': 2, 'dash_type': 'dash'},
            'fill':   {'color': '#FFFFC2'}
        })

        worksheet.insert_chart('C34', chart)

        workbook.close()
