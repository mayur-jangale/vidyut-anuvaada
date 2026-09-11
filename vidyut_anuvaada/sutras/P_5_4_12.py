# Sutra प.5.4.12: अमु च च्छन्दसि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — amu ca cCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.12"
SUTRA_TEXT = "अमु च च्छन्दसि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — amu ca cCandasi"


class Sutra5412:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.12: अग्निः'),
		('रामः', '', 'प.5.4.12: रामः'),
		('सीता', '', 'प.5.4.12: सीता'),
	]

