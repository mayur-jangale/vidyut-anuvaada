# Sutra प.1.4.88: अपपरी वर्जने
# (Samjna (technical definitions)) — apaparI varjane

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.88"
SUTRA_TEXT = "अपपरी वर्जने"
SUTRA_DESC = "(Samjna (technical definitions)) — apaparI varjane"


class Sutra1488:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_88
		return apply_1_4_88(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-apa-parI:अग्निः'),
		('रामः', '', 'not-apa-parI:रामः'),
		('सीता', '', 'not-apa-parI:सीता'),
	]

