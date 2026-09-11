# Sutra प.5.4.105: कुमहद्भ्यामन्यतरस्याम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kumahadByAmanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.105"
SUTRA_TEXT = "कुमहद्भ्यामन्यतरस्याम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kumahadByAmanyatarasyAm"


class Sutra54105:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.105: अग्निः'),
		('रामः', '', 'प.5.4.105: रामः'),
		('सीता', '', 'प.5.4.105: सीता'),
	]

