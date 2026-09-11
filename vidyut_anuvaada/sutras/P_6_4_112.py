# Sutra प.6.4.112: श्नाऽभ्यस्तयोरातः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.112"
SUTRA_TEXT = "श्नाऽभ्यस्तयोरातः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64112:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.112: अग्निः'),
		('रामः', '', 'प.6.4.112: रामः'),
		('सीता', '', 'प.6.4.112: सीता'),
	]

