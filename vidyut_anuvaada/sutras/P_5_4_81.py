# Sutra प.5.4.81: अन्ववतप्ताद्रहसः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — anvavataptAdrahasaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.81"
SUTRA_TEXT = "अन्ववतप्ताद्रहसः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — anvavataptAdrahasaH"


class Sutra5481:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.81: अग्निः'),
		('रामः', '', 'प.5.4.81: रामः'),
		('सीता', '', 'प.5.4.81: सीता'),
	]

