# Sutra प.7.3.98: रुदश्च पञ्चभ्यः
# (Taddhita (secondary derivations)) — rudaSca paYcaByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.98"
SUTRA_TEXT = "रुदश्च पञ्चभ्यः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — rudaSca paYcaByaH"


class Sutra7398:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.98: अग्निः'),
		('रामः', '', 'प.7.3.98: रामः'),
		('सीता', '', 'प.7.3.98: सीता'),
	]

