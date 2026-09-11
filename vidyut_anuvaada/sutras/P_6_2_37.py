# Sutra प.6.2.37: कार्तकौजपादयश्च
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.37"
SUTRA_TEXT = "कार्तकौजपादयश्च"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6237:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.37: अग्निः'),
		('रामः', '', 'प.6.2.37: रामः'),
		('सीता', '', 'प.6.2.37: सीता'),
	]

