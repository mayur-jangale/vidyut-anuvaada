# Sutra प.1.2.60: फल्गुनीप्रोष्ठपदानां च नक्षत्रे
# (Samjna (technical definitions)) — PalgunIprozWapadAnAM ca nakzatre

from P_1_2 import apply_1_2_60

SUTRA_CODE = "प.1.2.60"
SUTRA_TEXT = "फल्गुनीप्रोष्ठपदानां च नक्षत्रे"
SUTRA_DESC = "(Samjna (technical definitions)) — PalgunIprozWapadAnAM ca nakzatre"


class Sutra1260:
	def apply(self, word, pos):
		return apply_1_2_60(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-nakṣatra:अग्निः'),
		('रामः', '', 'non-nakṣatra:रामः'),
		('सीता', '', 'non-nakṣatra:सीता'),
	]

