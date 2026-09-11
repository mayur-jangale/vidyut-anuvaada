# Sutra प.7.1.37: समासेऽनञ्पूर्वे क्त्वो ल्यप्
# (Taddhita (secondary derivations)) — samAse'naYpUrve ktvo lyap

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.37"
SUTRA_TEXT = "समासेऽनञ्पूर्वे क्त्वो ल्यप्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — samAse'naYpUrve ktvo lyap"


class Sutra7137:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.37: अग्निः'),
		('रामः', '', 'प.7.1.37: रामः'),
		('सीता', '', 'प.7.1.37: सीता'),
	]

