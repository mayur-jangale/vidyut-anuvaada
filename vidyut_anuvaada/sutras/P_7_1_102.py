# Sutra प.7.1.102: उदोष्ठ्यपूर्वस्य
# (Taddhita (secondary derivations)) — udozWyapUrvasya

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.102"
SUTRA_TEXT = "उदोष्ठ्यपूर्वस्य"
SUTRA_DESC = "(Taddhita (secondary derivations)) — udozWyapUrvasya"


class Sutra71102:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.102: अग्निः'),
		('रामः', '', 'प.7.1.102: रामः'),
		('सीता', '', 'प.7.1.102: सीता'),
	]

