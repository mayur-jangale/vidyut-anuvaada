# Sutra प.7.2.103: किमः कः
# (Taddhita (secondary derivations)) — kimaH kaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.103"
SUTRA_TEXT = "किमः कः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — kimaH kaH"


class Sutra72103:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.103: अग्निः'),
		('रामः', '', 'प.7.2.103: रामः'),
		('सीता', '', 'प.7.2.103: सीता'),
	]

