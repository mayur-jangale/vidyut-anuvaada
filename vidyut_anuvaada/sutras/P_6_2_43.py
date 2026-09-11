# Sutra प.6.2.43: चतुर्थी तदर्थे
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.43"
SUTRA_TEXT = "चतुर्थी तदर्थे"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6243:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.43: अग्निः'),
		('रामः', '', 'प.6.2.43: रामः'),
		('सीता', '', 'प.6.2.43: सीता'),
	]

