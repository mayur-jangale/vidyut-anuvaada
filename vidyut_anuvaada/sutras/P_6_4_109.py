# Sutra प.6.4.109: ये च
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.109"
SUTRA_TEXT = "ये च"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64109:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.109: अग्निः'),
		('रामः', '', 'प.6.4.109: रामः'),
		('सीता', '', 'प.6.4.109: सीता'),
	]

