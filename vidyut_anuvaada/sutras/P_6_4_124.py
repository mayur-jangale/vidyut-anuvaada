# Sutra प.6.4.124: वा जॄभ्रमुत्रसाम्
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.124"
SUTRA_TEXT = "वा जॄभ्रमुत्रसाम्"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64124:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.124: अग्निः'),
		('रामः', '', 'प.6.4.124: रामः'),
		('सीता', '', 'प.6.4.124: सीता'),
	]

