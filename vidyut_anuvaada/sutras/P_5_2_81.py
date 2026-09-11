# Sutra प.5.2.81: कालप्रयोजनाद्रोगे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — kAlaprayojanAdroge

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.81"
SUTRA_TEXT = "कालप्रयोजनाद्रोगे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — kAlaprayojanAdroge"


class Sutra5281:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.81: अग्निः'),
		('रामः', '', 'प.5.2.81: रामः'),
		('सीता', '', 'प.5.2.81: सीता'),
	]

