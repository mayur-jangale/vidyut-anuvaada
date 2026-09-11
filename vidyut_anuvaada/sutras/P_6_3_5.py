# Sutra प.6.3.5: आज्ञायिनि च
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.5"
SUTRA_TEXT = "आज्ञायिनि च"
SUTRA_DESC = "final-sandhi — continued"


class Sutra635:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.5: अग्निः'),
		('रामः', '', 'प.6.3.5: रामः'),
		('सीता', '', 'प.6.3.5: सीता'),
	]

