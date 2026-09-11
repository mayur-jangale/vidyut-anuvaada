# Sutra प.7.2.35: आर्धधातुकस्येड् वलादेः
# (Taddhita (secondary derivations)) — ArDaDAtukasyeq valAdeH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.35"
SUTRA_TEXT = "आर्धधातुकस्येड् वलादेः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ArDaDAtukasyeq valAdeH"


class Sutra7235:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.35: अग्निः'),
		('रामः', '', 'प.7.2.35: रामः'),
		('सीता', '', 'प.7.2.35: सीता'),
	]

