# Sutra प.7.3.35: जनिवध्योश्च
# (Taddhita (secondary derivations)) — janivaDyoSca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.35"
SUTRA_TEXT = "जनिवध्योश्च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — janivaDyoSca"


class Sutra7335:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.35: अग्निः'),
		('रामः', '', 'प.7.3.35: रामः'),
		('सीता', '', 'प.7.3.35: सीता'),
	]

