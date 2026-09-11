# Sutra प.5.1.89: चित्तवति नित्यम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — cittavati nityam

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.89"
SUTRA_TEXT = "चित्तवति नित्यम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — cittavati nityam"


class Sutra5189:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.89: अग्निः'),
		('रामः', '', 'प.5.1.89: रामः'),
		('सीता', '', 'प.5.1.89: सीता'),
	]

