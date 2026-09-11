# Sutra प.6.2.31: दिष्टिवितस्त्योश्च
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.31"
SUTRA_TEXT = "दिष्टिवितस्त्योश्च"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6231:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.31: अग्निः'),
		('रामः', '', 'प.6.2.31: रामः'),
		('सीता', '', 'प.6.2.31: सीता'),
	]

