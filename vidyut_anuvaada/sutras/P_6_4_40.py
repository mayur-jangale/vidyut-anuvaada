# Sutra प.6.4.40: गमः क्वौ
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.40"
SUTRA_TEXT = "गमः क्वौ"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6440:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.40: अग्निः'),
		('रामः', '', 'प.6.4.40: रामः'),
		('सीता', '', 'प.6.4.40: सीता'),
	]

