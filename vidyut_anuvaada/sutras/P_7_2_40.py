# Sutra प.7.2.40: सिचि च परस्मैपदेषु
# (Taddhita (secondary derivations)) — sici ca parasmEpadezu

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.40"
SUTRA_TEXT = "सिचि च परस्मैपदेषु"
SUTRA_DESC = "(Taddhita (secondary derivations)) — sici ca parasmEpadezu"


class Sutra7240:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.40: अग्निः'),
		('रामः', '', 'प.7.2.40: रामः'),
		('सीता', '', 'प.7.2.40: सीता'),
	]

