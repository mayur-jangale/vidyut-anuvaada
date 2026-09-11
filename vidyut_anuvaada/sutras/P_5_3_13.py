# Sutra प.5.3.13: वा ह च च्छन्दसि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — vA ha ca cCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.13"
SUTRA_TEXT = "वा ह च च्छन्दसि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — vA ha ca cCandasi"


class Sutra5313:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.13: अग्निः'),
		('रामः', '', 'प.5.3.13: रामः'),
		('सीता', '', 'प.5.3.13: सीता'),
	]

