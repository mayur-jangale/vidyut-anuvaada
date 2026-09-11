# Sutra प.5.4.109: नपुंसकादन्यतरस्याम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — napuMsakAdanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.109"
SUTRA_TEXT = "नपुंसकादन्यतरस्याम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — napuMsakAdanyatarasyAm"


class Sutra54109:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.109: अग्निः'),
		('रामः', '', 'प.5.4.109: रामः'),
		('सीता', '', 'प.5.4.109: सीता'),
	]

