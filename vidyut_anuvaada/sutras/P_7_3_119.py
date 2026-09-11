# Sutra प.7.3.119: अच्च घेः
# (Taddhita (secondary derivations)) — acca GeH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.119"
SUTRA_TEXT = "अच्च घेः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — acca GeH"


class Sutra73119:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.119: अग्निः'),
		('रामः', '', 'प.7.3.119: रामः'),
		('सीता', '', 'प.7.3.119: सीता'),
	]

