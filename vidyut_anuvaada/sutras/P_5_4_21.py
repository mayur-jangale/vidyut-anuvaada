# Sutra प.5.4.21: तत्प्रकृतवचने मयट्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tatprakftavacane mayaw

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.21"
SUTRA_TEXT = "तत्प्रकृतवचने मयट्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tatprakftavacane mayaw"


class Sutra5421:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.21: अग्निः'),
		('रामः', '', 'प.5.4.21: रामः'),
		('सीता', '', 'प.5.4.21: सीता'),
	]

