# Sutra प.7.4.80: ओः पुयण्ज्यपरे
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.80"
SUTRA_TEXT = "ओः पुयण्ज्यपरे"
SUTRA_DESC = "taddhita — continued"


class Sutra7480:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.80: अग्निः'),
		('रामः', '', 'प.7.4.80: रामः'),
		('सीता', '', 'प.7.4.80: सीता'),
	]

