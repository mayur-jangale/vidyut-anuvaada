# Sutra प.7.4.92: ऋतश्च
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.92"
SUTRA_TEXT = "ऋतश्च"
SUTRA_DESC = "taddhita — continued"


class Sutra7492:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.92: अग्निः'),
		('रामः', '', 'प.7.4.92: रामः'),
		('सीता', '', 'प.7.4.92: सीता'),
	]

