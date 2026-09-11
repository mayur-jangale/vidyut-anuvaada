# Sutra प.6.2.14: मात्रोपज्ञोपक्रमच्छाये नपुंसके
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.14"
SUTRA_TEXT = "मात्रोपज्ञोपक्रमच्छाये नपुंसके"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6214:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.14: अग्निः'),
		('रामः', '', 'प.6.2.14: रामः'),
		('सीता', '', 'प.6.2.14: सीता'),
	]

