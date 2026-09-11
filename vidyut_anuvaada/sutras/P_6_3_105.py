# Sutra प.6.3.105: ईषदर्थे
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.105"
SUTRA_TEXT = "ईषदर्थे"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63105:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.105: अग्निः'),
		('रामः', '', 'प.6.3.105: रामः'),
		('सीता', '', 'प.6.3.105: सीता'),
	]

