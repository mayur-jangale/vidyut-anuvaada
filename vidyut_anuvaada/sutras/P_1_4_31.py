# Sutra प.1.4.31: भुवः प्रभवः
# (Samjna (technical definitions)) — BuvaH praBavaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.31"
SUTRA_TEXT = "भुवः प्रभवः"
SUTRA_DESC = "(Samjna (technical definitions)) — BuvaH praBavaH"


class Sutra1431:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_31
		return apply_1_4_31(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-bhU-apadana:अग्निः'),
		('रामः', '', 'not-bhU-apadana:रामः'),
		('सीता', '', 'not-bhU-apadana:सीता'),
	]

