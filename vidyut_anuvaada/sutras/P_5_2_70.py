# Sutra प.5.2.70: तन्त्रादचिरापहृते
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tantrAdacirApahfte

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.70"
SUTRA_TEXT = "तन्त्रादचिरापहृते"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tantrAdacirApahfte"


class Sutra5270:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.70: अग्निः'),
		('रामः', '', 'प.5.2.70: रामः'),
		('सीता', '', 'प.5.2.70: सीता'),
	]

