# Sutra प.6.2.23: सविधसनीडसमर्यादसवेशसदेशेषु सामीप्ये
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.23"
SUTRA_TEXT = "सविधसनीडसमर्यादसवेशसदेशेषु सामीप्ये"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6223:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.23: अग्निः'),
		('रामः', '', 'प.6.2.23: रामः'),
		('सीता', '', 'प.6.2.23: सीता'),
	]

