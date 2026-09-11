# Sutra प.8.4.45: यरोऽनुनासिकेऽनुनासिको वा
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.45"
SUTRA_TEXT = "यरोऽनुनासिकेऽनुनासिको वा"
SUTRA_DESC = "final transformations — continued"


class Sutra8445:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.45: अग्निः'),
		('रामः', '', 'प.8.4.45: रामः'),
		('सीता', '', 'प.8.4.45: सीता'),
	]

