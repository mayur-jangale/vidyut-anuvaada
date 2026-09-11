# Sutra प.7.2.43: ऋतश्च संयोगादेः
# (Taddhita (secondary derivations)) — ftaSca saMyogAdeH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.43"
SUTRA_TEXT = "ऋतश्च संयोगादेः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ftaSca saMyogAdeH"


class Sutra7243:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.43: अग्निः'),
		('रामः', '', 'प.7.2.43: रामः'),
		('सीता', '', 'प.7.2.43: सीता'),
	]

