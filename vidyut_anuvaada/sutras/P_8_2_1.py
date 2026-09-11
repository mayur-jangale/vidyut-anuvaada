# Sutra प.8.2.1: पूर्वत्रासिद्धम्
# pūrvatrāsiddham — earlier rule has no effect here (asiddhatva)

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.1"
SUTRA_TEXT = "पूर्वत्रासिद्धम्"
SUTRA_DESC = "pūrvatrāsiddham — earlier rule has no effect here (asiddhatva)"


class Sutra821:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.1: अग्निः'),
		('रामः', '', 'प.8.2.1: रामः'),
		('सीता', '', 'प.8.2.1: सीता'),
	]

