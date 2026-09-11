# Sutra प.7.3.4: द्वारादीनां च
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.4"
SUTRA_TEXT = "द्वारादीनां च"
SUTRA_DESC = "taddhita — continued"


class Sutra734:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.4: अग्निः'),
		('रामः', '', 'प.7.3.4: रामः'),
		('सीता', '', 'प.7.3.4: सीता'),
	]

