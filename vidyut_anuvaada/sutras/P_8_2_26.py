# Sutra प.8.2.26: झलो झलि
# aparaḥ paraṃ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.26"
SUTRA_TEXT = "झलो झलि"
SUTRA_DESC = "aparaḥ paraṃ — repeated"


class Sutra8226:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.26: अग्निः'),
		('रामः', '', 'प.8.2.26: रामः'),
		('सीता', '', 'प.8.2.26: सीता'),
	]

