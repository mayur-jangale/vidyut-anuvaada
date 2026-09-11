# Sutra प.6.4.132: वाह ऊठ्
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.132"
SUTRA_TEXT = "वाह ऊठ्"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64132:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.132: अग्निः'),
		('रामः', '', 'प.6.4.132: रामः'),
		('सीता', '', 'प.6.4.132: सीता'),
	]

