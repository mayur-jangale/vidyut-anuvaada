# Sutra प.6.4.75: बहुलं छन्दस्यमाङ्योगेऽपि
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.75"
SUTRA_TEXT = "बहुलं छन्दस्यमाङ्योगेऽपि"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6475:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.75: अग्निः'),
		('रामः', '', 'प.6.4.75: रामः'),
		('सीता', '', 'प.6.4.75: सीता'),
	]

