# Sutra प.1.4.72: विभाषा कृञि
# (Samjna (technical definitions)) — viBAzA kfYi

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.72"
SUTRA_TEXT = "विभाषा कृञि"
SUTRA_DESC = "(Samjna (technical definitions)) — viBAzA kfYi"


class Sutra1472:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_72
		return apply_1_4_72(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'no-optional:अग्निः'),
		('रामः', '', 'no-optional:रामः'),
		('सीता', '', 'no-optional:सीता'),
	]

