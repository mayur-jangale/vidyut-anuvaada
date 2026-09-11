# Sutra प.7.2.48: तीषसहलुभरुषरिषः
# (Taddhita (secondary derivations)) — tIzasahaluBaruzarizaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.48"
SUTRA_TEXT = "तीषसहलुभरुषरिषः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — tIzasahaluBaruzarizaH"


class Sutra7248:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.48: अग्निः'),
		('रामः', '', 'प.7.2.48: रामः'),
		('सीता', '', 'प.7.2.48: सीता'),
	]

