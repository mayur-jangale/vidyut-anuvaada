# Sutra प.8.3.12: कानाम्रेडिते
# ādeḥ aṅgasya — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.12"
SUTRA_TEXT = "कानाम्रेडिते"
SUTRA_DESC = "ādeḥ aṅgasya — repeated"


class Sutra8312:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.12: अग्निः'),
		('रामः', '', 'प.8.3.12: रामः'),
		('सीता', '', 'प.8.3.12: सीता'),
	]

