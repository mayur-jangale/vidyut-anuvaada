# Sutra प.5.3.99: जीविकार्थे चापण्ये
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — jIvikArTe cApaRye

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.99"
SUTRA_TEXT = "जीविकार्थे चापण्ये"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — jIvikArTe cApaRye"


class Sutra5399:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.99: अग्निः'),
		('रामः', '', 'प.5.3.99: रामः'),
		('सीता', '', 'प.5.3.99: सीता'),
	]

