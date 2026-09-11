# Sutra प.5.3.12: किमोऽत्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kimo't

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.12"
SUTRA_TEXT = "किमोऽत्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kimo't"


class Sutra5312:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.12: अग्निः'),
		('रामः', '', 'प.5.3.12: रामः'),
		('सीता', '', 'प.5.3.12: सीता'),
	]

