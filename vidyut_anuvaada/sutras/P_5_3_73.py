# Sutra प.5.3.73: अज्ञाते
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — ajYAte

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.73"
SUTRA_TEXT = "अज्ञाते"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — ajYAte"


class Sutra5373:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.73: अग्निः'),
		('रामः', '', 'प.5.3.73: रामः'),
		('सीता', '', 'प.5.3.73: सीता'),
	]

