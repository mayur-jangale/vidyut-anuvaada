# Sutra प.1.2.44: एकविभक्ति चापूर्वनिपाते
# (Samjna (technical definitions)) — ekaviBakti cApUrvanipAte

from P_1_2 import apply_1_2_44

SUTRA_CODE = "प.1.2.44"
SUTRA_TEXT = "एकविभक्ति चापूर्वनिपाते"
SUTRA_DESC = "(Samjna (technical definitions)) — ekaviBakti cApUrvanipAte"


class Sutra1244:
	def apply(self, word, pos):
		return apply_1_2_44(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-eka-vibhakti:अग्निः'),
		('रामः', '', 'non-eka-vibhakti:रामः'),
		('सीता', '', 'non-eka-vibhakti:सीता'),
	]

