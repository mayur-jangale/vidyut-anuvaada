# Sutra प.7.2.100: अचि र ऋतः
# (Taddhita (secondary derivations)) — aci ra ftaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.100"
SUTRA_TEXT = "अचि र ऋतः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — aci ra ftaH"


class Sutra72100:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.100: अग्निः'),
		('रामः', '', 'प.7.2.100: रामः'),
		('सीता', '', 'प.7.2.100: सीता'),
	]

