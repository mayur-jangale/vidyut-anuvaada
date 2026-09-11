# Sutra प.7.4.53: यीवर्णयोर्दीधीवेव्योः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.53"
SUTRA_TEXT = "यीवर्णयोर्दीधीवेव्योः"
SUTRA_DESC = "taddhita — continued"


class Sutra7453:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.53: अग्निः'),
		('रामः', '', 'प.7.4.53: रामः'),
		('सीता', '', 'प.7.4.53: सीता'),
	]

