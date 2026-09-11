# Sutra प.7.1.41: लोपस्त आत्मनेपदेषु
# (Taddhita (secondary derivations)) — lopasta Atmanepadezu

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.41"
SUTRA_TEXT = "लोपस्त आत्मनेपदेषु"
SUTRA_DESC = "(Taddhita (secondary derivations)) — lopasta Atmanepadezu"


class Sutra7141:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.41: अग्निः'),
		('रामः', '', 'प.7.1.41: रामः'),
		('सीता', '', 'प.7.1.41: सीता'),
	]

