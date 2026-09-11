# Sutra प.1.4.46: अधिशीङ्स्थाऽऽसां कर्म
# (Samjna (technical definitions)) — aDiSINsTA''sAM karma

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.46"
SUTRA_TEXT = "अधिशीङ्स्थाऽऽसां कर्म"
SUTRA_DESC = "(Samjna (technical definitions)) — aDiSINsTA''sAM karma"


class Sutra1446:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_46
		return apply_1_4_46(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-aDi-karman:अग्निः'),
		('रामः', '', 'not-aDi-karman:रामः'),
		('सीता', '', 'not-aDi-karman:सीता'),
	]

