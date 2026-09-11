# Sutra प.1.4.10: ह्रस्वं लघु
# (Samjna (technical definitions)) — hrasvaM laGu

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.10"
SUTRA_TEXT = "ह्रस्वं लघु"
SUTRA_DESC = "(Samjna (technical definitions)) — hrasvaM laGu"


class Sutra1410:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_10
		return apply_1_4_10(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-laghu:अग्निः'),
		('रामः', '', 'not-laghu:रामः'),
		('सीता', '', 'not-laghu:सीता'),
	]

