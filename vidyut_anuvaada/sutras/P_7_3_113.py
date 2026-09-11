# Sutra प.7.3.113: याडापः
# (Taddhita (secondary derivations)) — yAqApaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.113"
SUTRA_TEXT = "याडापः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — yAqApaH"


class Sutra73113:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.113: अग्निः'),
		('रामः', '', 'प.7.3.113: रामः'),
		('सीता', '', 'प.7.3.113: सीता'),
	]

