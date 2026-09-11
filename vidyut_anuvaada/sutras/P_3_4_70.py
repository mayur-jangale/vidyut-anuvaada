# Sutra प.3.4.70: तयोरेव कृत्यक्तखलर्थाः
# gāṭ — specific agent noun formation

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.70"
SUTRA_TEXT = "तयोरेव कृत्यक्तखलर्थाः"
SUTRA_DESC = "gāṭ — specific agent noun formation"


class Sutra3470:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

