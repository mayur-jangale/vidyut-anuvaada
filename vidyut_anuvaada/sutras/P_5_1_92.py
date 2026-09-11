# Sutra प.5.1.92: सम्परिपूर्वात् ख च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — samparipUrvAt Ka ca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.92"
SUTRA_TEXT = "सम्परिपूर्वात् ख च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — samparipUrvAt Ka ca"


class Sutra5192:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.92: अग्निः'),
		('रामः', '', 'प.5.1.92: रामः'),
		('सीता', '', 'प.5.1.92: सीता'),
	]

