# Sutra प.5.3.33: पश्च पश्चा च च्छन्दसि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — paSca paScA ca cCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.33"
SUTRA_TEXT = "पश्च पश्चा च च्छन्दसि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — paSca paScA ca cCandasi"


class Sutra5333:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.33: अग्निः'),
		('रामः', '', 'प.5.3.33: रामः'),
		('सीता', '', 'प.5.3.33: सीता'),
	]

