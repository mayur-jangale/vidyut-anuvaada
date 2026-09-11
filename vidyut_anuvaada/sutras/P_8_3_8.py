# Sutra प.8.3.8: उभयथर्क्षु
# ādeḥ aṅgasya — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.8"
SUTRA_TEXT = "उभयथर्क्षु"
SUTRA_DESC = "ādeḥ aṅgasya — repeated"


class Sutra838:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.8: अग्निः'),
		('रामः', '', 'प.8.3.8: रामः'),
		('सीता', '', 'प.8.3.8: सीता'),
	]

