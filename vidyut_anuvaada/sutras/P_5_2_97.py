# Sutra प.5.2.97: सिध्मादिभ्यश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — siDmAdiByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.97"
SUTRA_TEXT = "सिध्मादिभ्यश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — siDmAdiByaSca"


class Sutra5297:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.97: अग्निः'),
		('रामः', '', 'प.5.2.97: रामः'),
		('सीता', '', 'प.5.2.97: सीता'),
	]

