# Sutra प.6.4.148: यस्येति च
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.148"
SUTRA_TEXT = "यस्येति च"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64148:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.148: अग्निः'),
		('रामः', '', 'प.6.4.148: रामः'),
		('सीता', '', 'प.6.4.148: सीता'),
	]

