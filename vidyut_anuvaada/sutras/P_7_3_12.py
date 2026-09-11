# Sutra प.7.3.12: सुसर्वार्धाज्जनपदस्य
# (Taddhita (secondary derivations)) — susarvArDAjjanapadasya

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.12"
SUTRA_TEXT = "सुसर्वार्धाज्जनपदस्य"
SUTRA_DESC = "(Taddhita (secondary derivations)) — susarvArDAjjanapadasya"


class Sutra7312:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.12: अग्निः'),
		('रामः', '', 'प.7.3.12: रामः'),
		('सीता', '', 'प.7.3.12: सीता'),
	]

