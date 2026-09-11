# Sutra प.7.3.64: ओक उचः के
# (Taddhita (secondary derivations)) — oka ucaH ke

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.64"
SUTRA_TEXT = "ओक उचः के"
SUTRA_DESC = "(Taddhita (secondary derivations)) — oka ucaH ke"


class Sutra7364:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.64: अग्निः'),
		('रामः', '', 'प.7.3.64: रामः'),
		('सीता', '', 'प.7.3.64: सीता'),
	]

