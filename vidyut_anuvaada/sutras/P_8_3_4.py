# Sutra प.8.3.4: अनुनासिकात् परोऽनुस्वारः
# ādeḥ aṅgasya — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.4"
SUTRA_TEXT = "अनुनासिकात् परोऽनुस्वारः"
SUTRA_DESC = "ādeḥ aṅgasya — repeated"


class Sutra834:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.4: अग्निः'),
		('रामः', '', 'प.8.3.4: रामः'),
		('सीता', '', 'प.8.3.4: सीता'),
	]

