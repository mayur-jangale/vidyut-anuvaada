# Sutra प.7.1.64: लभेश्च
# (Taddhita (secondary derivations)) — laBeSca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.64"
SUTRA_TEXT = "लभेश्च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — laBeSca"


class Sutra7164:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.64: अग्निः'),
		('रामः', '', 'प.7.1.64: रामः'),
		('सीता', '', 'प.7.1.64: सीता'),
	]

