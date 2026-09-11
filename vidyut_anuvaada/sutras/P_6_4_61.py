# Sutra प.6.4.61: वाक्रोशदैन्ययोः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.61"
SUTRA_TEXT = "वाक्रोशदैन्ययोः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6461:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.61: अग्निः'),
		('रामः', '', 'प.6.4.61: रामः'),
		('सीता', '', 'प.6.4.61: सीता'),
	]

