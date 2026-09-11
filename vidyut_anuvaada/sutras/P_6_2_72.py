# Sutra प.6.2.72: गोबिडालसिंहसैन्धवेषूपमाने
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.72"
SUTRA_TEXT = "गोबिडालसिंहसैन्धवेषूपमाने"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6272:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.72: अग्निः'),
		('रामः', '', 'प.6.2.72: रामः'),
		('सीता', '', 'प.6.2.72: सीता'),
	]

