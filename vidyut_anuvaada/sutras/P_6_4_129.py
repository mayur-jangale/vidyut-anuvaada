# Sutra प.6.4.129: भस्य
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.129"
SUTRA_TEXT = "भस्य"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64129:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.129: अग्निः'),
		('रामः', '', 'प.6.4.129: रामः'),
		('सीता', '', 'प.6.4.129: सीता'),
	]

