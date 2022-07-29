import time

class DateUtil():
	@staticmethod
	def format(self, date_digi):
	#2000/1/1 36526 946656000
	time_stamp = (date_digi - 36526) * 24 * 60 * 60 + 946656000
	return time.strftime("%Y-%m-%d", time.localtime(time_stamp))
	
