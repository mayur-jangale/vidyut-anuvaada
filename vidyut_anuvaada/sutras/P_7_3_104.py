# Sutra प.7.3.104: ओसि च
# (Taddhita (secondary derivations)) — osi ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.104"
SUTRA_TEXT = "ओसि च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — osi ca"


class Sutra73104:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.104: अग्निः'),
		('रामः', '', 'प.7.3.104: रामः'),
		('सीता', '', 'प.7.3.104: सीता'),
	]

