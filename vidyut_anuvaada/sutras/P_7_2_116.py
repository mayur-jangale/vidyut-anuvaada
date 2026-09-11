# Sutra प.7.2.116: अत उपधायाः
# (Taddhita (secondary derivations)) — ata upaDAyAH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.116"
SUTRA_TEXT = "अत उपधायाः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ata upaDAyAH"


class Sutra72116:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.116: अग्निः'),
		('रामः', '', 'प.7.2.116: रामः'),
		('सीता', '', 'प.7.2.116: सीता'),
	]

