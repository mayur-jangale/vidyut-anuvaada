# Sutra प.6.4.110: अत उत् सार्वधातुके
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.110"
SUTRA_TEXT = "अत उत् सार्वधातुके"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64110:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.110: अग्निः'),
		('रामः', '', 'प.6.4.110: रामः'),
		('सीता', '', 'प.6.4.110: सीता'),
	]

