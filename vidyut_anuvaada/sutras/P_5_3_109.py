# Sutra प.5.3.109: एकशालायाष्ठजन्यतरस्याम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ekaSAlAyAzWajanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.109"
SUTRA_TEXT = "एकशालायाष्ठजन्यतरस्याम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ekaSAlAyAzWajanyatarasyAm"


class Sutra53109:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.109: अग्निः'),
		('रामः', '', 'प.5.3.109: रामः'),
		('सीता', '', 'प.5.3.109: सीता'),
	]

