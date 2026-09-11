# Sutra प.6.4.94: खचि ह्रस्वः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.94"
SUTRA_TEXT = "खचि ह्रस्वः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6494:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.94: अग्निः'),
		('रामः', '', 'प.6.4.94: रामः'),
		('सीता', '', 'प.6.4.94: सीता'),
	]

