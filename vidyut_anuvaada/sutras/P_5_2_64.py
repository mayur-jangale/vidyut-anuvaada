# Sutra प.5.2.64: आकर्षादिभ्यः कन्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — AkarzAdiByaH kan

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.64"
SUTRA_TEXT = "आकर्षादिभ्यः कन्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — AkarzAdiByaH kan"


class Sutra5264:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.64: अग्निः'),
		('रामः', '', 'प.5.2.64: रामः'),
		('सीता', '', 'प.5.2.64: सीता'),
	]

