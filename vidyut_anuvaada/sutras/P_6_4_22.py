# Sutra प.6.4.22: असिद्धवदत्राभात्
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.22"
SUTRA_TEXT = "असिद्धवदत्राभात्"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6422:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.22: अग्निः'),
		('रामः', '', 'प.6.4.22: रामः'),
		('सीता', '', 'प.6.4.22: सीता'),
	]

