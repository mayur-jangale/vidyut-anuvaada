# Sutra प.7.3.99: अड्गार्ग्यगालवयोः
# (Taddhita (secondary derivations)) — aqgArgyagAlavayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.99"
SUTRA_TEXT = "अड्गार्ग्यगालवयोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — aqgArgyagAlavayoH"


class Sutra7399:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.99: अग्निः'),
		('रामः', '', 'प.7.3.99: रामः'),
		('सीता', '', 'प.7.3.99: सीता'),
	]

