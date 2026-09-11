# Sutra प.8.4.56: वाऽवसाने
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.56"
SUTRA_TEXT = "वाऽवसाने"
SUTRA_DESC = "final transformations — continued"


class Sutra8456:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.56: अग्निः'),
		('रामः', '', 'प.8.4.56: रामः'),
		('सीता', '', 'प.8.4.56: सीता'),
	]

