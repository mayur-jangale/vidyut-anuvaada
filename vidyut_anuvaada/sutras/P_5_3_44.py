# Sutra प.5.3.44: एकाद्धो ध्यमुञन्यतरस्याम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ekAdDo DyamuYanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.44"
SUTRA_TEXT = "एकाद्धो ध्यमुञन्यतरस्याम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ekAdDo DyamuYanyatarasyAm"


class Sutra5344:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.44: अग्निः'),
		('रामः', '', 'प.5.3.44: रामः'),
		('सीता', '', 'प.5.3.44: सीता'),
	]

