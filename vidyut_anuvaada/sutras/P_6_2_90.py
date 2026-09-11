# Sutra प.6.2.90: अर्मे चावर्णं द्व्यच्त्र्यच्
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.90"
SUTRA_TEXT = "अर्मे चावर्णं द्व्यच्त्र्यच्"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6290:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.90: अग्निः'),
		('रामः', '', 'प.6.2.90: रामः'),
		('सीता', '', 'प.6.2.90: सीता'),
	]

