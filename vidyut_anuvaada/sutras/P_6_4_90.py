# Sutra प.6.4.90: दोषो णौ
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.90"
SUTRA_TEXT = "दोषो णौ"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6490:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.90: अग्निः'),
		('रामः', '', 'प.6.4.90: रामः'),
		('सीता', '', 'प.6.4.90: सीता'),
	]

