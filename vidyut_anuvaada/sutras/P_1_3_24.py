# Sutra प.1.3.24: उदोऽनूर्ध्वकर्मणि
from P_1_3 import apply_1_3_24


class Sutra1324:
	def apply(self, word, pos):
		return apply_1_3_24(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'udoUrDvakarmaNi:अग्निः;n/a'),
		('रामः', '', 'udoUrDvakarmaNi:रामः;n/a'),
		('सीता', '', 'udoUrDvakarmaNi:सीता;n/a'),
	]

