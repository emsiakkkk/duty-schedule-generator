if __name__ == '__main__':
	path = r'./excel/2022年8月班表20220729.xlsx' #替换为当月的班表，xlsx格式
	schedule = Monthly_Duty_Schedule('2022年8月', path)
	output_file = r'./excel/20220728121955_2022年08月值班计划模板表.xlsx' #替换为当月的班表
	writer = Duty_Schedule_Writer(output_file, schedule)
	writer.write_duty_schedule_detail()
