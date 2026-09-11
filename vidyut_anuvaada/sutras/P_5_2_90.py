# Sutra प.5.2.90: अनुपद्यन्वेष्टा
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — anupadyanvezwA

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.90"
SUTRA_TEXT = "अनुपद्यन्वेष्टा"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — anupadyanvezwA"


class Sutra5290:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.90: अग्निः'),
		('रामः', '', 'प.5.2.90: रामः'),
		('सीता', '', 'प.5.2.90: सीता'),
	]

