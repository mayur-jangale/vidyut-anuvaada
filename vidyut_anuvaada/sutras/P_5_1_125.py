# Sutra प.5.1.125: स्तेनाद्यन्नलोपश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — stenAdyannalopaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.125"
SUTRA_TEXT = "स्तेनाद्यन्नलोपश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — stenAdyannalopaSca"


class Sutra51125:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.125: अग्निः'),
		('रामः', '', 'प.5.1.125: रामः'),
		('सीता', '', 'प.5.1.125: सीता'),
	]

