# Sutra प.8.3.3: आतोऽटि नित्यम्
# aṅgasya — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.3"
SUTRA_TEXT = "आतोऽटि नित्यम्"
SUTRA_DESC = "aṅgasya — continued"


class Sutra833:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.3: अग्निः'),
		('रामः', '', 'प.8.3.3: रामः'),
		('सीता', '', 'प.8.3.3: सीता'),
	]

