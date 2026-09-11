# Sutra प.6.4.17: तनोतेर्विभाषा
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.17"
SUTRA_TEXT = "तनोतेर्विभाषा"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6417:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.17: अग्निः'),
		('रामः', '', 'प.6.4.17: रामः'),
		('सीता', '', 'प.6.4.17: सीता'),
	]

