# Sutra प.6.2.68: पापं च शिल्पिनि
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.68"
SUTRA_TEXT = "पापं च शिल्पिनि"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6268:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.68: अग्निः'),
		('रामः', '', 'प.6.2.68: रामः'),
		('सीता', '', 'प.6.2.68: सीता'),
	]

