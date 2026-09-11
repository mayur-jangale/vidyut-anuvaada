# Sutra प.7.3.102: सुपि च
# (Taddhita (secondary derivations)) — supi ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.102"
SUTRA_TEXT = "सुपि च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — supi ca"


class Sutra73102:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.102: अग्निः'),
		('रामः', '', 'प.7.3.102: रामः'),
		('सीता', '', 'प.7.3.102: सीता'),
	]

