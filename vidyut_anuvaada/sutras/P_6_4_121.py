# Sutra प.6.4.121: थलि च सेटि
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.121"
SUTRA_TEXT = "थलि च सेटि"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64121:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.121: अग्निः'),
		('रामः', '', 'प.6.4.121: रामः'),
		('सीता', '', 'प.6.4.121: सीता'),
	]

