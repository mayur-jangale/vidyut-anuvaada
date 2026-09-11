# Sutra प.6.4.60: निष्ठायामण्यदर्थे
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.60"
SUTRA_TEXT = "निष्ठायामण्यदर्थे"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6460:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.60: अग्निः'),
		('रामः', '', 'प.6.4.60: रामः'),
		('सीता', '', 'प.6.4.60: सीता'),
	]

