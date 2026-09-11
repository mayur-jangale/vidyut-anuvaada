# Sutra प.8.4.61: उदः स्थास्तम्भोः पूर्वस्य
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.61"
SUTRA_TEXT = "उदः स्थास्तम्भोः पूर्वस्य"
SUTRA_DESC = "final transformations — continued"


class Sutra8461:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.61: अग्निः'),
		('रामः', '', 'प.8.4.61: रामः'),
		('सीता', '', 'प.8.4.61: सीता'),
	]

