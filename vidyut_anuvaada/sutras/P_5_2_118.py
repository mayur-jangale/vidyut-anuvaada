# Sutra प.5.2.118: एकगोपूर्वाट्ठञ् नित्यम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ekagopUrvAwWaY nityam

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.118"
SUTRA_TEXT = "एकगोपूर्वाट्ठञ् नित्यम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ekagopUrvAwWaY nityam"


class Sutra52118:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.118: अग्निः'),
		('रामः', '', 'प.5.2.118: रामः'),
		('सीता', '', 'प.5.2.118: सीता'),
	]

