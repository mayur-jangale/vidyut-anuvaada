# Sutra प.7.2.22: कृच्छ्रगहनयोः कषः
# (Taddhita (secondary derivations)) — kfcCragahanayoH kazaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.22"
SUTRA_TEXT = "कृच्छ्रगहनयोः कषः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — kfcCragahanayoH kazaH"


class Sutra7222:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.22: अग्निः'),
		('रामः', '', 'प.7.2.22: रामः'),
		('सीता', '', 'प.7.2.22: सीता'),
	]

