# Sutra प.5.4.49: रोगाच्चापनयने
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — rogAccApanayane

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.49"
SUTRA_TEXT = "रोगाच्चापनयने"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — rogAccApanayane"


class Sutra5449:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.49: अग्निः'),
		('रामः', '', 'प.5.4.49: रामः'),
		('सीता', '', 'प.5.4.49: सीता'),
	]

