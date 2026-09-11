# Sutra प.7.3.70: घोर्लोपो लेटि वा
# (Taddhita (secondary derivations)) — Gorlopo lewi vA

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.70"
SUTRA_TEXT = "घोर्लोपो लेटि वा"
SUTRA_DESC = "(Taddhita (secondary derivations)) — Gorlopo lewi vA"


class Sutra7370:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.70: अग्निः'),
		('रामः', '', 'प.7.3.70: रामः'),
		('सीता', '', 'प.7.3.70: सीता'),
	]

