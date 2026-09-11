# Sutra प.5.4.63: सुखप्रियादानुलोम्ये
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — suKapriyAdAnulomye

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.63"
SUTRA_TEXT = "सुखप्रियादानुलोम्ये"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — suKapriyAdAnulomye"


class Sutra5463:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.63: अग्निः'),
		('रामः', '', 'प.5.4.63: रामः'),
		('सीता', '', 'प.5.4.63: सीता'),
	]

