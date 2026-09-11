# Sutra प.6.4.38: वा ल्यपि
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.38"
SUTRA_TEXT = "वा ल्यपि"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6438:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.38: अग्निः'),
		('रामः', '', 'प.6.4.38: रामः'),
		('सीता', '', 'प.6.4.38: सीता'),
	]

