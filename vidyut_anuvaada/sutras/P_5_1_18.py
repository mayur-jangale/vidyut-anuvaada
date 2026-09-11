# Sutra प.5.1.18: प्राग्वतेष्ठञ्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — prAgvatezWaY

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.18"
SUTRA_TEXT = "प्राग्वतेष्ठञ्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — prAgvatezWaY"


class Sutra5118:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.18: अग्निः'),
		('रामः', '', 'प.5.1.18: रामः'),
		('सीता', '', 'प.5.1.18: सीता'),
	]

