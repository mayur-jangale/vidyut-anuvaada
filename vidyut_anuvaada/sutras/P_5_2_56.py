# Sutra प.5.2.56: विंशत्यादिभ्यस्तमडन्यतरस्याम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — viMSatyAdiByastamaqanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.56"
SUTRA_TEXT = "विंशत्यादिभ्यस्तमडन्यतरस्याम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — viMSatyAdiByastamaqanyatarasyAm"


class Sutra5256:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.56: अग्निः'),
		('रामः', '', 'प.5.2.56: रामः'),
		('सीता', '', 'प.5.2.56: सीता'),
	]

