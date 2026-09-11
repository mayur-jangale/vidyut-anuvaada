# Sutra प.5.4.66: सत्यादशपथे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — satyAdaSapaTe

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.66"
SUTRA_TEXT = "सत्यादशपथे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — satyAdaSapaTe"


class Sutra5466:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.66: अग्निः'),
		('रामः', '', 'प.5.4.66: रामः'),
		('सीता', '', 'प.5.4.66: सीता'),
	]

