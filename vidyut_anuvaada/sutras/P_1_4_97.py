# Sutra प.1.4.97: अधिरीश्वरे
# (Samjna (technical definitions)) — aDirISvare

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.97"
SUTRA_TEXT = "अधिरीश्वरे"
SUTRA_DESC = "(Samjna (technical definitions)) — aDirISvare"


class Sutra1497:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_97
		return apply_1_4_97(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-adhi-ISvara:अग्निः'),
		('रामः', '', 'not-adhi-ISvara:रामः'),
		('सीता', '', 'not-adhi-ISvara:सीता'),
	]

