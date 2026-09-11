# Sutra प.7.4.45: सुधितवसुधितनेमधितधिष्वधिषीय च
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.45"
SUTRA_TEXT = "सुधितवसुधितनेमधितधिष्वधिषीय च"
SUTRA_DESC = "taddhita — continued"


class Sutra7445:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.45: अग्निः'),
		('रामः', '', 'प.7.4.45: रामः'),
		('सीता', '', 'प.7.4.45: सीता'),
	]

