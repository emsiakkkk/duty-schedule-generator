import time, re

class Util():
	@staticmethod
	def format_date(date_digi):
		#2000/1/1 36526 946656000
		time_stamp = (date_digi - 36526) * 24 * 60 * 60 + 946656000
		return time.strftime("%Y-%m-%d", time.localtime(time_stamp))
	
	@staticmethod
	def format_name(names):
		def _format_name(name):
			if name is None:
				return None
			result = re.search(r'[(（]+(.+?)[)）]+', name)
			return 	result.group(1) if result else name

		return list(map(_format_name, names))