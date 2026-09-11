# Sutra प.6.4.91: वा चित्तविरागे
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.91"
SUTRA_TEXT = "वा चित्तविरागे"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6491:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.91: अग्निः'),
		('रामः', '', 'प.6.4.91: रामः'),
		('सीता', '', 'प.6.4.91: सीता'),
	]

