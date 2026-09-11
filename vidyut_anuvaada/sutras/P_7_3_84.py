# Sutra प.7.3.84: सार्वधातुकार्धधातुकयोः
# (Taddhita (secondary derivations)) — sArvaDAtukArDaDAtukayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.84"
SUTRA_TEXT = "सार्वधातुकार्धधातुकयोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — sArvaDAtukArDaDAtukayoH"


class Sutra7384:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.84: अग्निः'),
		('रामः', '', 'प.7.3.84: रामः'),
		('सीता', '', 'प.7.3.84: सीता'),
	]

