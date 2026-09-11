# Sutra प.8.3.6: पुमः खय्यम्परे
# ādeḥ aṅgasya — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.6"
SUTRA_TEXT = "पुमः खय्यम्परे"
SUTRA_DESC = "ādeḥ aṅgasya — repeated"


class Sutra836:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.6: अग्निः'),
		('रामः', '', 'प.8.3.6: रामः'),
		('सीता', '', 'प.8.3.6: सीता'),
	]

