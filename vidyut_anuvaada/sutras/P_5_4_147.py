# Sutra प.5.4.147: त्रिककुत् पर्वते
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — trikakut parvate

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.147"
SUTRA_TEXT = "त्रिककुत् पर्वते"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — trikakut parvate"


class Sutra54147:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.147: अग्निः'),
		('रामः', '', 'प.5.4.147: रामः'),
		('सीता', '', 'प.5.4.147: सीता'),
	]

