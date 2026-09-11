# Sutra प.7.3.22: नेन्द्रस्य परस्य
# (Taddhita (secondary derivations)) — nendrasya parasya

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.22"
SUTRA_TEXT = "नेन्द्रस्य परस्य"
SUTRA_DESC = "(Taddhita (secondary derivations)) — nendrasya parasya"


class Sutra7322:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.22: अग्निः'),
		('रामः', '', 'प.7.3.22: रामः'),
		('सीता', '', 'प.7.3.22: सीता'),
	]

