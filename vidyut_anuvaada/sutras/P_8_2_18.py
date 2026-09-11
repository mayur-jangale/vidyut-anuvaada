# Sutra प.8.2.18: कृपो रो लः
# aparaḥ paraṃ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.18"
SUTRA_TEXT = "कृपो रो लः"
SUTRA_DESC = "aparaḥ paraṃ — repeated"


class Sutra8218:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.18: अग्निः'),
		('रामः', '', 'प.8.2.18: रामः'),
		('सीता', '', 'प.8.2.18: सीता'),
	]

