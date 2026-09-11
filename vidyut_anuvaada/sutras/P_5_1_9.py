# Sutra प.5.1.9: आत्मन्विश्वजनभोगोत्तरपदात् खः
# strīpratyaya — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.9"
SUTRA_TEXT = "आत्मन्विश्वजनभोगोत्तरपदात् खः"
SUTRA_DESC = "strīpratyaya — continued"


class Sutra519:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.9: अग्निः'),
		('रामः', '', 'प.5.1.9: रामः'),
		('सीता', '', 'प.5.1.9: सीता'),
	]

