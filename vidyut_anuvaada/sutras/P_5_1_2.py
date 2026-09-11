# Sutra प.5.1.2: उगवादिभ्यो यत्
# strīpratyaya — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.2"
SUTRA_TEXT = "उगवादिभ्यो यत्"
SUTRA_DESC = "strīpratyaya — continued"


class Sutra512:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.2: अग्निः'),
		('रामः', '', 'प.5.1.2: रामः'),
		('सीता', '', 'प.5.1.2: सीता'),
	]

