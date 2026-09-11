# Sutra प.8.4.47: अनचि च
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.47"
SUTRA_TEXT = "अनचि च"
SUTRA_DESC = "final transformations — continued"


class Sutra8447:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.47: अग्निः'),
		('रामः', '', 'प.8.4.47: रामः'),
		('सीता', '', 'प.8.4.47: सीता'),
	]

