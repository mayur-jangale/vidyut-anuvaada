# Sutra प.7.1.52: आमि सर्वनाम्नः सुट्
# (Taddhita (secondary derivations)) — Ami sarvanAmnaH suw

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.52"
SUTRA_TEXT = "आमि सर्वनाम्नः सुट्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — Ami sarvanAmnaH suw"


class Sutra7152:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.52: अग्निः'),
		('रामः', '', 'प.7.1.52: रामः'),
		('सीता', '', 'प.7.1.52: सीता'),
	]

