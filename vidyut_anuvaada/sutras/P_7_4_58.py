# Sutra प.7.4.58: अत्र लोपोऽभ्यासस्य
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.58"
SUTRA_TEXT = "अत्र लोपोऽभ्यासस्य"
SUTRA_DESC = "taddhita — continued"


class Sutra7458:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.58: अग्निः'),
		('रामः', '', 'प.7.4.58: रामः'),
		('सीता', '', 'प.7.4.58: सीता'),
	]

