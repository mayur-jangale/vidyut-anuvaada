# Sutra प.7.4.68: व्यथो लिटि
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.68"
SUTRA_TEXT = "व्यथो लिटि"
SUTRA_DESC = "taddhita — continued"


class Sutra7468:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.68: अग्निः'),
		('रामः', '', 'प.7.4.68: रामः'),
		('सीता', '', 'प.7.4.68: सीता'),
	]

