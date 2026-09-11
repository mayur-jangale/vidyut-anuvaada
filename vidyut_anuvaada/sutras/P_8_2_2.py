# Sutra प.8.2.2: नलोपः सुप्स्वरसंज्ञातुग्विधिषु कृति
# uttaratrāsiddham — later rule has no effect here

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.2"
SUTRA_TEXT = "नलोपः सुप्स्वरसंज्ञातुग्विधिषु कृति"
SUTRA_DESC = "uttaratrāsiddham — later rule has no effect here"


class Sutra822:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.2: अग्निः'),
		('रामः', '', 'प.8.2.2: रामः'),
		('सीता', '', 'प.8.2.2: सीता'),
	]

