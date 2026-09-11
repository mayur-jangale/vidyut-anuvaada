# Sutra प.6.4.86: छन्दस्युभयथा
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.86"
SUTRA_TEXT = "छन्दस्युभयथा"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6486:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.86: अग्निः'),
		('रामः', '', 'प.6.4.86: रामः'),
		('सीता', '', 'प.6.4.86: सीता'),
	]

