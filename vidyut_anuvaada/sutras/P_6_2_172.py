# Sutra प.6.2.172: नञ्सुभ्याम्
# (Sandhi (euphonic combination)) — naYsuByAm

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.172"
SUTRA_TEXT = "नञ्सुभ्याम्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — naYsuByAm"


class Sutra62172:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.172: अग्निः'),
		('रामः', '', 'प.6.2.172: रामः'),
		('सीता', '', 'प.6.2.172: सीता'),
	]

