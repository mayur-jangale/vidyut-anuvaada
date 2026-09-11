# Sutra प.6.4.139: उद ईत्
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.139"
SUTRA_TEXT = "उद ईत्"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64139:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.139: अग्निः'),
		('रामः', '', 'प.6.4.139: रामः'),
		('सीता', '', 'प.6.4.139: सीता'),
	]

