from duty_schedule.monthly_duty_schedule import Monthly_Duty_Schedule 
from writer.duty_schedule_writer import Duty_Schedule_Writer

					
if __name__ == '__main__':
	path = r'./excel/2022年8月班表20220729.xlsx' #原始班表
	schedule = Monthly_Duty_Schedule('2022年8月', path)
	# print(schedule.staff("李五"))
	output_file = r'./excel/20220728121955_2022年08月值班计划模板表.xlsx' #下载当月的空白模板
	writer = Duty_Schedule_Writer(output_file, schedule)
	writer.write_duty_schedule_detail()

	# TODO 起止日期的检查、适配 1日~30/31日
	