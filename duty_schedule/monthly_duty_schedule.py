import os
from reader.duty_schedule_reader import Duty_Schedule_Reader
#from duty_schedule.daily_duty_schedule import Daily_Duty_Schedule 

class Monthly_Duty_Schedule(object):
	"""docstring for Monthly_Duty_Schedule"""
	def __init__(self, month, path):
		super(Monthly_Duty_Schedule, self).__init__()
		self.month = month
		self._reader = Duty_Schedule_Reader(path)
		self.schedule = {}
		self.all_staffs = []
		for d in self._reader:
			self.schedule[d.date] = d
			self._add_staff(d.staffs)


	def _add_staff(self, staffs):
		for s in staffs:
			if s not in self.all_staffs:
				self.all_staffs.append(s)				

	def get(self, date):
		#校验date
		return self.schedule[date]

	def last_date(self):
		date_keys = self.schedule.keys()
		return date_keys

	# 返回当月指定值班人员值班情况
	def staff(self, staff_name):
		staff_schedule = {}
		if staff_name in self.all_staffs:
			for date, daily_schedule in self.schedule.items():
				#print(date)
				staff_schedule[date] = []
				if staff_name in daily_schedule.morning:
					staff_schedule[date].append(0)
					#print('早')
				if staff_name in daily_schedule.afernoon:
					staff_schedule[date].append(1)
					#print('中')
				if staff_name in daily_schedule.evening:
					staff_schedule[date].append(2)
					#print('晚')	
			
			#return {staff_name : staff_schedule}
			return staff_schedule	
				# print(date)
				# print(daily_schedule)

