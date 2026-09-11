# Sutra प.7.2.81: आतो ङितः
# (Taddhita (secondary derivations)) — Ato NitaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.81"
SUTRA_TEXT = "आतो ङितः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — Ato NitaH"


class Sutra7281:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.81: अग्निः'),
		('रामः', '', 'प.7.2.81: रामः'),
		('सीता', '', 'प.7.2.81: सीता'),
	]

