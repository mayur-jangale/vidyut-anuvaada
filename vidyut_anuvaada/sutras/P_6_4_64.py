# Sutra प.6.4.64: आतो लोप इटि च
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.64"
SUTRA_TEXT = "आतो लोप इटि च"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6464:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.64: अग्निः'),
		('रामः', '', 'प.6.4.64: रामः'),
		('सीता', '', 'प.6.4.64: सीता'),
	]

