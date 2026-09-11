# Sutra प.5.1.91: वत्सरान्ताच्छश्छन्दसि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vatsarAntAcCaSCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.91"
SUTRA_TEXT = "वत्सरान्ताच्छश्छन्दसि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vatsarAntAcCaSCandasi"


class Sutra5191:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.91: अग्निः'),
		('रामः', '', 'प.5.1.91: रामः'),
		('सीता', '', 'प.5.1.91: सीता'),
	]

