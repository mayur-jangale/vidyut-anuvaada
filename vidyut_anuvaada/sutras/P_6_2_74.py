# Sutra प.6.2.74: प्राचां क्रीडायाम्
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.74"
SUTRA_TEXT = "प्राचां क्रीडायाम्"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6274:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.74: अग्निः'),
		('रामः', '', 'प.6.2.74: रामः'),
		('सीता', '', 'प.6.2.74: सीता'),
	]

