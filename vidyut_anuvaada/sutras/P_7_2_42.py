# Sutra प.7.2.42: लिङ्सिचोरात्मनेपदेषु
# (Taddhita (secondary derivations)) — liNsicorAtmanepadezu

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.42"
SUTRA_TEXT = "लिङ्सिचोरात्मनेपदेषु"
SUTRA_DESC = "(Taddhita (secondary derivations)) — liNsicorAtmanepadezu"


class Sutra7242:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.42: अग्निः'),
		('रामः', '', 'प.7.2.42: रामः'),
		('सीता', '', 'प.7.2.42: सीता'),
	]

