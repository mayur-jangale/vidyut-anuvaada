# Sutra प.5.1.26: शूर्पादञन्यतरस्याम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — SUrpAdaYanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.26"
SUTRA_TEXT = "शूर्पादञन्यतरस्याम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — SUrpAdaYanyatarasyAm"


class Sutra5126:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.26: अग्निः'),
		('रामः', '', 'प.5.1.26: रामः'),
		('सीता', '', 'प.5.1.26: सीता'),
	]

