# Sutra प.7.3.32: हनस्तोऽचिण्णलोः
# (Taddhita (secondary derivations)) — hanasto'ciRRaloH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.32"
SUTRA_TEXT = "हनस्तोऽचिण्णलोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — hanasto'ciRRaloH"


class Sutra7332:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.32: अग्निः'),
		('रामः', '', 'प.7.3.32: रामः'),
		('सीता', '', 'प.7.3.32: सीता'),
	]

