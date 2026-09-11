# Sutra प.5.1.53: आढकाचितपात्रात् खोऽन्यतरस्याम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — AQakAcitapAtrAt Ko'nyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.53"
SUTRA_TEXT = "आढकाचितपात्रात् खोऽन्यतरस्याम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — AQakAcitapAtrAt Ko'nyatarasyAm"


class Sutra5153:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.53: अग्निः'),
		('रामः', '', 'प.5.1.53: रामः'),
		('सीता', '', 'प.5.1.53: सीता'),
	]

