# Sutra प.8.3.10: नॄन् पे
# ādeḥ aṅgasya — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.10"
SUTRA_TEXT = "नॄन् पे"
SUTRA_DESC = "ādeḥ aṅgasya — repeated"


class Sutra8310:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.10: अग्निः'),
		('रामः', '', 'प.8.3.10: रामः'),
		('सीता', '', 'प.8.3.10: सीता'),
	]

