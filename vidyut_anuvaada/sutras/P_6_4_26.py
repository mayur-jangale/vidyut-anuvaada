# Sutra प.6.4.26: रञ्जेश्च
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.26"
SUTRA_TEXT = "रञ्जेश्च"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6426:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.26: अग्निः'),
		('रामः', '', 'प.6.4.26: रामः'),
		('सीता', '', 'प.6.4.26: सीता'),
	]

