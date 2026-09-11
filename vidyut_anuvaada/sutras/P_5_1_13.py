# Sutra प.5.1.13: छदिरुपधिबलेर्ढञ्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — CadirupaDibalerQaY

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.13"
SUTRA_TEXT = "छदिरुपधिबलेर्ढञ्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — CadirupaDibalerQaY"


class Sutra5113:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.13: अग्निः'),
		('रामः', '', 'प.5.1.13: रामः'),
		('सीता', '', 'प.5.1.13: सीता'),
	]

