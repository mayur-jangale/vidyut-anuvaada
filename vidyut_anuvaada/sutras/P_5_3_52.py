# Sutra प.5.3.52: एकादाकिनिच्चासहाये
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ekAdAkiniccAsahAye

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.52"
SUTRA_TEXT = "एकादाकिनिच्चासहाये"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ekAdAkiniccAsahAye"


class Sutra5352:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.52: अग्निः'),
		('रामः', '', 'प.5.3.52: रामः'),
		('सीता', '', 'प.5.3.52: सीता'),
	]

