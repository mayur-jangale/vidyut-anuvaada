# Sutra प.7.2.72: स्तुसुधूञ्भ्यः परस्मैपदेषु
# (Taddhita (secondary derivations)) — stusuDUYByaH parasmEpadezu

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.72"
SUTRA_TEXT = "स्तुसुधूञ्भ्यः परस्मैपदेषु"
SUTRA_DESC = "(Taddhita (secondary derivations)) — stusuDUYByaH parasmEpadezu"


class Sutra7272:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.72: अग्निः'),
		('रामः', '', 'प.7.2.72: रामः'),
		('सीता', '', 'प.7.2.72: सीता'),
	]

