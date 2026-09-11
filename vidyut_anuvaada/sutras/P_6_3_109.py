# Sutra प.6.3.109: पृषोदरादीनि यथोपदिष्टम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.109"
SUTRA_TEXT = "पृषोदरादीनि यथोपदिष्टम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63109:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.109: अग्निः'),
		('रामः', '', 'प.6.3.109: रामः'),
		('सीता', '', 'प.6.3.109: सीता'),
	]

