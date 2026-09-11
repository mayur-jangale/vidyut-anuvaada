# Sutra प.6.4.101: हुझल्भ्यो हेर्धिः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.101"
SUTRA_TEXT = "हुझल्भ्यो हेर्धिः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64101:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.101: अग्निः'),
		('रामः', '', 'प.6.4.101: रामः'),
		('सीता', '', 'प.6.4.101: सीता'),
	]

