# Sutra प.8.2.17: नाद्घस्य
# paraḥ paraṃ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.17"
SUTRA_TEXT = "नाद्घस्य"
SUTRA_DESC = "paraḥ paraṃ — repeated"


class Sutra8217:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.17: अग्निः'),
		('रामः', '', 'प.8.2.17: रामः'),
		('सीता', '', 'प.8.2.17: सीता'),
	]

