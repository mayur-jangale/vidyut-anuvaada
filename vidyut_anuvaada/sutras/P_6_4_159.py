# Sutra प.6.4.159: इष्ठस्य यिट् च
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.159"
SUTRA_TEXT = "इष्ठस्य यिट् च"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64159:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.159: अग्निः'),
		('रामः', '', 'प.6.4.159: रामः'),
		('सीता', '', 'प.6.4.159: सीता'),
	]

