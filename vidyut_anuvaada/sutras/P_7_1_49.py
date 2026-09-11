# Sutra प.7.1.49: स्नात्व्यादयश्च
# (Taddhita (secondary derivations)) — snAtvyAdayaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.49"
SUTRA_TEXT = "स्नात्व्यादयश्च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — snAtvyAdayaSca"


class Sutra7149:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.49: अग्निः'),
		('रामः', '', 'प.7.1.49: रामः'),
		('सीता', '', 'प.7.1.49: सीता'),
	]

