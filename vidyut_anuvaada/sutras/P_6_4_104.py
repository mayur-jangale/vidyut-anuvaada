# Sutra प.6.4.104: चिणो लुक्
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.104"
SUTRA_TEXT = "चिणो लुक्"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64104:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.104: अग्निः'),
		('रामः', '', 'प.6.4.104: रामः'),
		('सीता', '', 'प.6.4.104: सीता'),
	]

