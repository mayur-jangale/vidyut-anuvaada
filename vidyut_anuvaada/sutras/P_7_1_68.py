# Sutra प.7.1.68: न सुदुर्भ्यां केवलाभ्याम्
# (Taddhita (secondary derivations)) — na sudurByAM kevalAByAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.68"
SUTRA_TEXT = "न सुदुर्भ्यां केवलाभ्याम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — na sudurByAM kevalAByAm"


class Sutra7168:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.68: अग्निः'),
		('रामः', '', 'प.7.1.68: रामः'),
		('सीता', '', 'प.7.1.68: सीता'),
	]

