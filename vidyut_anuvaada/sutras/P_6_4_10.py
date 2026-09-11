# Sutra प.6.4.10: सान्तमहतः संयोगस्य
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.10"
SUTRA_TEXT = "सान्तमहतः संयोगस्य"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6410:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.10: अग्निः'),
		('रामः', '', 'प.6.4.10: रामः'),
		('सीता', '', 'प.6.4.10: सीता'),
	]

