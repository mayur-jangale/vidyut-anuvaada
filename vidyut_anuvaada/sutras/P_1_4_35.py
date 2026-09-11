# Sutra प.1.4.35: धारेरुत्तमर्णः
# (Samjna (technical definitions)) — DAreruttamarRaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.35"
SUTRA_TEXT = "धारेरुत्तमर्णः"
SUTRA_DESC = "(Samjna (technical definitions)) — DAreruttamarRaH"


class Sutra1435:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_35
		return apply_1_4_35(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-dhAra-sampradAnam:अग्निः'),
		('रामः', '', 'not-dhAra-sampradAnam:रामः'),
		('सीता', '', 'not-dhAra-sampradAnam:सीता'),
	]

