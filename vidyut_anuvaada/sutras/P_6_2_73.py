# Sutra प.6.2.73: अके जीविकाऽर्थे
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.73"
SUTRA_TEXT = "अके जीविकाऽर्थे"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6273:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.73: अग्निः'),
		('रामः', '', 'प.6.2.73: रामः'),
		('सीता', '', 'प.6.2.73: सीता'),
	]

