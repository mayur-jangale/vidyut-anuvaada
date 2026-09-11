# Sutra प.6.4.3: नामि
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.3"
SUTRA_TEXT = "नामि"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra643:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.3: अग्निः'),
		('रामः', '', 'प.6.4.3: रामः'),
		('सीता', '', 'प.6.4.3: सीता'),
	]

