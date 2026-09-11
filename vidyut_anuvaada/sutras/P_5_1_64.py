# Sutra प.5.1.64: छेदादिभ्यो नित्यम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — CedAdiByo nityam

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.64"
SUTRA_TEXT = "छेदादिभ्यो नित्यम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — CedAdiByo nityam"


class Sutra5164:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.64: अग्निः'),
		('रामः', '', 'प.5.1.64: रामः'),
		('सीता', '', 'प.5.1.64: सीता'),
	]

