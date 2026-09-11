# Sutra प.5.1.61: सप्तनोऽञ् छन्दसि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — saptano'Y Candasi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.61"
SUTRA_TEXT = "सप्तनोऽञ् छन्दसि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — saptano'Y Candasi"


class Sutra5161:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.61: अग्निः'),
		('रामः', '', 'प.5.1.61: रामः'),
		('सीता', '', 'प.5.1.61: सीता'),
	]

