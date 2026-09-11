# Sutra प.7.1.29: शसो न
# (Taddhita (secondary derivations)) — Saso na

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.29"
SUTRA_TEXT = "शसो न"
SUTRA_DESC = "(Taddhita (secondary derivations)) — Saso na"


class Sutra7129:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.29: अग्निः'),
		('रामः', '', 'प.7.1.29: रामः'),
		('सीता', '', 'प.7.1.29: सीता'),
	]

