# Sutra प.7.2.109: दश्च
# (Taddhita (secondary derivations)) — daSca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.109"
SUTRA_TEXT = "दश्च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — daSca"


class Sutra72109:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.109: अग्निः'),
		('रामः', '', 'प.7.2.109: रामः'),
		('सीता', '', 'प.7.2.109: सीता'),
	]

