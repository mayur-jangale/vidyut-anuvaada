# Sutra प.7.2.80: अतो येयः
# (Taddhita (secondary derivations)) — ato yeyaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.80"
SUTRA_TEXT = "अतो येयः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ato yeyaH"


class Sutra7280:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.80: अग्निः'),
		('रामः', '', 'प.7.2.80: रामः'),
		('सीता', '', 'प.7.2.80: सीता'),
	]

