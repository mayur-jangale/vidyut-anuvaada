# Sutra प.6.2.55: हिरण्यपरिमाणं धने
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.55"
SUTRA_TEXT = "हिरण्यपरिमाणं धने"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6255:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.55: अग्निः'),
		('रामः', '', 'प.6.2.55: रामः'),
		('सीता', '', 'प.6.2.55: सीता'),
	]

