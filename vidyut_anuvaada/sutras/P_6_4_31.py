# Sutra प.6.4.31: क्त्वि स्कन्दिस्यन्दोः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.31"
SUTRA_TEXT = "क्त्वि स्कन्दिस्यन्दोः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6431:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.31: अग्निः'),
		('रामः', '', 'प.6.4.31: रामः'),
		('सीता', '', 'प.6.4.31: सीता'),
	]

