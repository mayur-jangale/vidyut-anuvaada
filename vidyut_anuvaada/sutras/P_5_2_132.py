# Sutra प.5.2.132: धर्मशीलवर्णान्ताच्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — DarmaSIlavarRAntAcca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.132"
SUTRA_TEXT = "धर्मशीलवर्णान्ताच्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — DarmaSIlavarRAntAcca"


class Sutra52132:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.132: अग्निः'),
		('रामः', '', 'प.5.2.132: रामः'),
		('सीता', '', 'प.5.2.132: सीता'),
	]

