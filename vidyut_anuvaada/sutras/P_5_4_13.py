# Sutra प.5.4.13: अनुगादिनष्ठक्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — anugAdinazWak

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.13"
SUTRA_TEXT = "अनुगादिनष्ठक्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — anugAdinazWak"


class Sutra5413:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.13: अग्निः'),
		('रामः', '', 'प.5.4.13: रामः'),
		('सीता', '', 'प.5.4.13: सीता'),
	]

