import time

class Daily_Duty_Schedule(object):
	"""docstring for Daily_Duty_Schedule"""
	#有无调班情况、日期变数字、值班班长、通宵班单岗还是双岗 TODO
	def __init__(self, date, day_of_week, evening : list, morning : list, afernoon : list):
		super(Daily_Duty_Schedule, self).__init__()
		self.date = self._format_date(date)
		self.day_of_week = day_of_week
		self.evening = evening
		self.morning = morning
		self.afernoon = afernoon
		self.staffs = list(filter(None, [self.morning[0], self.morning[1], self.afernoon[0], self.afernoon[1], self.evening[0], self.evening[1]]))

	def _format_date(self, date_digi):
		#2000/1/1 36526 946656000
		time_stamp = (date_digi - 36526) * 24 * 60 * 60 + 946656000
		return time.strftime("%Y-%m-%d", time.localtime(time_stamp))
	
	def __str__(self):
		return '{0}    {1}    {2}    {3}    {4}    {5}    {6}    {7}'.format(self.date, self.day_of_week, self.morning[0], self.morning[1], self.afernoon[0], self.afernoon[1], self.evening[0], self.evening[1])

