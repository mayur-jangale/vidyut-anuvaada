# Sutra प.7.1.34: आत औ णलः
# (Taddhita (secondary derivations)) — Ata O RalaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.34"
SUTRA_TEXT = "आत औ णलः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — Ata O RalaH"


class Sutra7134:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.34: अग्निः'),
		('रामः', '', 'प.7.1.34: रामः'),
		('सीता', '', 'प.7.1.34: सीता'),
	]

