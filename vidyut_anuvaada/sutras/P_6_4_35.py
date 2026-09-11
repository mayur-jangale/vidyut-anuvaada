# Sutra प.6.4.35: शा हौ
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.35"
SUTRA_TEXT = "शा हौ"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6435:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.35: अग्निः'),
		('रामः', '', 'प.6.4.35: रामः'),
		('सीता', '', 'प.6.4.35: सीता'),
	]

