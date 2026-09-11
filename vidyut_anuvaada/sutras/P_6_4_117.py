# Sutra प.6.4.117: आ च हौ
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.117"
SUTRA_TEXT = "आ च हौ"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64117:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.117: अग्निः'),
		('रामः', '', 'प.6.4.117: रामः'),
		('सीता', '', 'प.6.4.117: सीता'),
	]

