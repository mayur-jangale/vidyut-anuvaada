# Sutra प.1.2.14: हनः सिच्
# (Samjna (technical definitions)) — hanaH sic

from P_1_2 import apply_1_2_14

SUTRA_CODE = "प.1.2.14"
SUTRA_TEXT = "हनः सिच्"
SUTRA_DESC = "(Samjna (technical definitions)) — hanaH sic"


class Sutra1214:
	def apply(self, word, pos):
		return apply_1_2_14(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-han:अग्निः'),
		('रामः', '', 'non-han:रामः'),
		('सीता', '', 'non-han:सीता'),
	]

