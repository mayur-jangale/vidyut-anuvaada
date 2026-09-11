# Sutra प.6.2.19: न भूवाक्चिद्दिधिषु
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.19"
SUTRA_TEXT = "न भूवाक्चिद्दिधिषु"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6219:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.19: अग्निः'),
		('रामः', '', 'प.6.2.19: रामः'),
		('सीता', '', 'प.6.2.19: सीता'),
	]

