# Sutra प.5.4.103: अनसन्तान्नपुंसकाच्छन्दसि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — anasantAnnapuMsakAcCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.103"
SUTRA_TEXT = "अनसन्तान्नपुंसकाच्छन्दसि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — anasantAnnapuMsakAcCandasi"


class Sutra54103:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.103: अग्निः'),
		('रामः', '', 'प.5.4.103: रामः'),
		('सीता', '', 'प.5.4.103: सीता'),
	]

