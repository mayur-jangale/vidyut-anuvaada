# Sutra प.7.3.5: न्यग्रोधस्य च केवलस्य
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.5"
SUTRA_TEXT = "न्यग्रोधस्य च केवलस्य"
SUTRA_DESC = "taddhita — continued"


class Sutra735:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.5: अग्निः'),
		('रामः', '', 'प.7.3.5: रामः'),
		('सीता', '', 'प.7.3.5: सीता'),
	]

