# Sutra प.6.2.81: युक्तारोह्यादयश्च
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.81"
SUTRA_TEXT = "युक्तारोह्यादयश्च"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6281:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.81: अग्निः'),
		('रामः', '', 'प.6.2.81: रामः'),
		('सीता', '', 'प.6.2.81: सीता'),
	]

