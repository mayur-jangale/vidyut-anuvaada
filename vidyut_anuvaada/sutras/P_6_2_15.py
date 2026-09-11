# Sutra प.6.2.15: सुखप्रिययोर्हिते
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.15"
SUTRA_TEXT = "सुखप्रिययोर्हिते"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6215:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.15: अग्निः'),
		('रामः', '', 'प.6.2.15: रामः'),
		('सीता', '', 'प.6.2.15: सीता'),
	]

