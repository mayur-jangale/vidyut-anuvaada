# Sutra प.1.2.24: वञ्चिलुञ्च्यृतश्च
# (Samjna (technical definitions)) — vaYciluYcyftaSca

from P_1_2 import apply_1_2_24

SUTRA_CODE = "प.1.2.24"
SUTRA_TEXT = "वञ्चिलुञ्च्यृतश्च"
SUTRA_DESC = "(Samjna (technical definitions)) — vaYciluYcyftaSca"


class Sutra1224:
	def apply(self, word, pos):
		return apply_1_2_24(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-vañci:अग्निः'),
		('रामः', '', 'non-vañci:रामः'),
		('सीता', '', 'non-vañci:सीता'),
	]

