# Sutra प.5.4.34: विनयादिभ्यष्ठक्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vinayAdiByazWak

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.34"
SUTRA_TEXT = "विनयादिभ्यष्ठक्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vinayAdiByazWak"


class Sutra5434:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.34: अग्निः'),
		('रामः', '', 'प.5.4.34: रामः'),
		('सीता', '', 'प.5.4.34: सीता'),
	]

