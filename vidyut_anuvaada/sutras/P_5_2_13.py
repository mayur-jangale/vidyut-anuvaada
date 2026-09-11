# Sutra प.5.2.13: अद्यश्वीनाऽवष्टब्धे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — adyaSvInA'vazwabDe

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.13"
SUTRA_TEXT = "अद्यश्वीनाऽवष्टब्धे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — adyaSvInA'vazwabDe"


class Sutra5213:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.13: अग्निः'),
		('रामः', '', 'प.5.2.13: रामः'),
		('सीता', '', 'प.5.2.13: सीता'),
	]

