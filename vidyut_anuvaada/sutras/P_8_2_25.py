# Sutra प.8.2.25: धि च
# paraḥ paraṃ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.25"
SUTRA_TEXT = "धि च"
SUTRA_DESC = "paraḥ paraṃ — repeated"


class Sutra8225:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.25: अग्निः'),
		('रामः', '', 'प.8.2.25: रामः'),
		('सीता', '', 'प.8.2.25: सीता'),
	]

