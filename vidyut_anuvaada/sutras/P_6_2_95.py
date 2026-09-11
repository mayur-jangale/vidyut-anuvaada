# Sutra प.6.2.95: कुमार्यां वयसि
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.95"
SUTRA_TEXT = "कुमार्यां वयसि"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6295:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.95: अग्निः'),
		('रामः', '', 'प.6.2.95: रामः'),
		('सीता', '', 'प.6.2.95: सीता'),
	]

