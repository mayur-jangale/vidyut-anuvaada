# Sutra प.7.2.107: अदस औ सुलोपश्च
# (Taddhita (secondary derivations)) — adasa O sulopaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.107"
SUTRA_TEXT = "अदस औ सुलोपश्च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — adasa O sulopaSca"


class Sutra72107:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.107: अग्निः'),
		('रामः', '', 'प.7.2.107: रामः'),
		('सीता', '', 'प.7.2.107: सीता'),
	]

