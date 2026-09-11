# Sutra प.5.4.19: एकस्य सकृच्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ekasya sakfcca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.19"
SUTRA_TEXT = "एकस्य सकृच्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ekasya sakfcca"


class Sutra5419:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.19: अग्निः'),
		('रामः', '', 'प.5.4.19: रामः'),
		('सीता', '', 'प.5.4.19: सीता'),
	]

