# Sutra प.8.4.40: स्तोः श्चुना श्चुः
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.40"
SUTRA_TEXT = "स्तोः श्चुना श्चुः"
SUTRA_DESC = "final transformations — continued"


class Sutra8440:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.40: अग्निः'),
		('रामः', '', 'प.8.4.40: रामः'),
		('सीता', '', 'प.8.4.40: सीता'),
	]

