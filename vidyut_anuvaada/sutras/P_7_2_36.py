# Sutra प.7.2.36: स्नुक्रमोरनात्मनेपदनिमित्ते
# (Taddhita (secondary derivations)) — snukramoranAtmanepadanimitte

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.36"
SUTRA_TEXT = "स्नुक्रमोरनात्मनेपदनिमित्ते"
SUTRA_DESC = "(Taddhita (secondary derivations)) — snukramoranAtmanepadanimitte"


class Sutra7236:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.36: अग्निः'),
		('रामः', '', 'प.7.2.36: रामः'),
		('सीता', '', 'प.7.2.36: सीता'),
	]

