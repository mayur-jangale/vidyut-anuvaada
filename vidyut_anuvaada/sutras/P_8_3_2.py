# Sutra प.8.3.2: अत्रानुनासिकः पूर्वस्य तु वा
# ādeḥ aṅgasya — beginning of aṅga

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.2"
SUTRA_TEXT = "अत्रानुनासिकः पूर्वस्य तु वा"
SUTRA_DESC = "ādeḥ aṅgasya — beginning of aṅga"


class Sutra832:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.2: अग्निः'),
		('रामः', '', 'प.8.3.2: रामः'),
		('सीता', '', 'प.8.3.2: सीता'),
	]

