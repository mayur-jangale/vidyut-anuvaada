# Sutra प.6.2.48: तृतीया कर्मणि
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.48"
SUTRA_TEXT = "तृतीया कर्मणि"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6248:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.48: अग्निः'),
		('रामः', '', 'प.6.2.48: रामः'),
		('सीता', '', 'प.6.2.48: सीता'),
	]

