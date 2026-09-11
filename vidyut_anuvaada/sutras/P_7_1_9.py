# Sutra प.7.1.9: अतो भिस ऐस्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.9"
SUTRA_TEXT = "अतो भिस ऐस्"
SUTRA_DESC = "taddhita — continued"


class Sutra719:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.9: अग्निः'),
		('रामः', '', 'प.7.1.9: रामः'),
		('सीता', '', 'प.7.1.9: सीता'),
	]

