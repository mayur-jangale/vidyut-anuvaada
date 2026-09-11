# Sutra प.6.4.18: क्रमश्च क्त्वि
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.18"
SUTRA_TEXT = "क्रमश्च क्त्वि"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6418:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.18: अग्निः'),
		('रामः', '', 'प.6.4.18: रामः'),
		('सीता', '', 'प.6.4.18: सीता'),
	]

