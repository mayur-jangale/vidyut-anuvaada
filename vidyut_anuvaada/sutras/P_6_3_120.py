# Sutra प.6.3.120: शरादीनां च
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.120"
SUTRA_TEXT = "शरादीनां च"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63120:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.120: अग्निः'),
		('रामः', '', 'प.6.3.120: रामः'),
		('सीता', '', 'प.6.3.120: सीता'),
	]

