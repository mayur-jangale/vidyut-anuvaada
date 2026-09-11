# Sutra प.6.4.100: घसिभसोर्हलि च
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.100"
SUTRA_TEXT = "घसिभसोर्हलि च"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64100:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.100: अग्निः'),
		('रामः', '', 'प.6.4.100: रामः'),
		('सीता', '', 'प.6.4.100: सीता'),
	]

