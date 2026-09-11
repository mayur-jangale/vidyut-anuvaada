# Sutra प.5.1.10: सर्वपुरुषाभ्यां णढञौ
# strīpratyaya — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.10"
SUTRA_TEXT = "सर्वपुरुषाभ्यां णढञौ"
SUTRA_DESC = "strīpratyaya — continued"


class Sutra5110:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.10: अग्निः'),
		('रामः', '', 'प.5.1.10: रामः'),
		('सीता', '', 'प.5.1.10: सीता'),
	]

