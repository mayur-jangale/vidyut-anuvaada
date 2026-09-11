# Sutra प.5.3.21: अनद्यतने र्हिलन्यतरस्याम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — anadyatane rhilanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.21"
SUTRA_TEXT = "अनद्यतने र्हिलन्यतरस्याम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — anadyatane rhilanyatarasyAm"


class Sutra5321:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.21: अग्निः'),
		('रामः', '', 'प.5.3.21: रामः'),
		('सीता', '', 'प.5.3.21: सीता'),
	]

