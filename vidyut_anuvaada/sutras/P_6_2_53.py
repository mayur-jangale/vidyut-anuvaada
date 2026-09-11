# Sutra प.6.2.53: न्यधी च
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.53"
SUTRA_TEXT = "न्यधी च"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6253:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.53: अग्निः'),
		('रामः', '', 'प.6.2.53: रामः'),
		('सीता', '', 'प.6.2.53: सीता'),
	]

