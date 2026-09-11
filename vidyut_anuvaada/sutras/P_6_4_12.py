# Sutra प.6.4.12: इन्हन्पूषार्यम्णां शौ
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.12"
SUTRA_TEXT = "इन्हन्पूषार्यम्णां शौ"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6412:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.12: अग्निः'),
		('रामः', '', 'प.6.4.12: रामः'),
		('सीता', '', 'प.6.4.12: सीता'),
	]

