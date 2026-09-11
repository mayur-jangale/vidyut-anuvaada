# Sutra प.6.2.91: न भूताधिकसंजीवमद्राश्मकज्जलम्
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.91"
SUTRA_TEXT = "न भूताधिकसंजीवमद्राश्मकज्जलम्"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6291:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.91: अग्निः'),
		('रामः', '', 'प.6.2.91: रामः'),
		('सीता', '', 'प.6.2.91: सीता'),
	]

