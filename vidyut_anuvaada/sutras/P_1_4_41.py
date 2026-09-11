# Sutra प.1.4.41: अनुप्रतिगृणश्च
# (Samjna (technical definitions)) — anupratigfRaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.41"
SUTRA_TEXT = "अनुप्रतिगृणश्च"
SUTRA_DESC = "(Samjna (technical definitions)) — anupratigfRaSca"


class Sutra1441:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_41
		return apply_1_4_41(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-anupratigR-kartA:अग्निः'),
		('रामः', '', 'not-anupratigR-kartA:रामः'),
		('सीता', '', 'not-anupratigR-kartA:सीता'),
	]

