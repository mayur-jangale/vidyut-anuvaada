# Sutra प.6.2.67: विभाषाऽध्यक्षे
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.67"
SUTRA_TEXT = "विभाषाऽध्यक्षे"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6267:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.67: अग्निः'),
		('रामः', '', 'प.6.2.67: रामः'),
		('सीता', '', 'प.6.2.67: सीता'),
	]

