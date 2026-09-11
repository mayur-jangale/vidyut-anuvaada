# Sutra प.5.2.131: सुखादिभ्यश्च
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — suKAdiByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.131"
SUTRA_TEXT = "सुखादिभ्यश्च"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — suKAdiByaSca"


class Sutra52131:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.131: अग्निः'),
		('रामः', '', 'प.5.2.131: रामः'),
		('सीता', '', 'प.5.2.131: सीता'),
	]

