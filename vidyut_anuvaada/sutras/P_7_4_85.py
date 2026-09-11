# Sutra प.7.4.85: नुगतोऽनुनासिकान्तस्य
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.85"
SUTRA_TEXT = "नुगतोऽनुनासिकान्तस्य"
SUTRA_DESC = "taddhita — continued"


class Sutra7485:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.85: अग्निः'),
		('रामः', '', 'प.7.4.85: रामः'),
		('सीता', '', 'प.7.4.85: सीता'),
	]

