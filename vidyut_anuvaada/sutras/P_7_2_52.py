# Sutra प.7.2.52: वसतिक्षुधोरिट्
# (Taddhita (secondary derivations)) — vasatikzuDoriw

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.52"
SUTRA_TEXT = "वसतिक्षुधोरिट्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — vasatikzuDoriw"


class Sutra7252:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.52: अग्निः'),
		('रामः', '', 'प.7.2.52: रामः'),
		('सीता', '', 'प.7.2.52: सीता'),
	]

