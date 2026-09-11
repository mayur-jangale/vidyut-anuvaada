# Sutra प.1.4.69: अच्छ गत्यर्थवदेषु
# (Samjna (technical definitions)) — acCa gatyarTavadezu

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.69"
SUTRA_TEXT = "अच्छ गत्यर्थवदेषु"
SUTRA_DESC = "(Samjna (technical definitions)) — acCa gatyarTavadezu"


class Sutra1469:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_69
		return apply_1_4_69(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-acCa:अग्निः'),
		('रामः', '', 'not-acCa:रामः'),
		('सीता', '', 'not-acCa:सीता'),
	]

