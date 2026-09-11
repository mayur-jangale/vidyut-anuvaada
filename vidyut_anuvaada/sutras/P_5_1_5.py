# Sutra प.5.1.5: तस्मै हितम्
# strīpratyaya — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.5"
SUTRA_TEXT = "तस्मै हितम्"
SUTRA_DESC = "strīpratyaya — continued"


class Sutra515:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.5: अग्निः'),
		('रामः', '', 'प.5.1.5: रामः'),
		('सीता', '', 'प.5.1.5: सीता'),
	]

