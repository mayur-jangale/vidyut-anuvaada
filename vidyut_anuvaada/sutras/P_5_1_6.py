# Sutra प.5.1.6: शरीरावयवाद्यत्
# strīpratyaya — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.6"
SUTRA_TEXT = "शरीरावयवाद्यत्"
SUTRA_DESC = "strīpratyaya — continued"


class Sutra516:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.6: अग्निः'),
		('रामः', '', 'प.5.1.6: रामः'),
		('सीता', '', 'प.5.1.6: सीता'),
	]

