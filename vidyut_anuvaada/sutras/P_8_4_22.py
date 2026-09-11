# Sutra प.8.4.22: हन्तेरत्पूर्वस्य
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.22"
SUTRA_TEXT = "हन्तेरत्पूर्वस्य"
SUTRA_DESC = "final transformations — continued"


class Sutra8422:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.22: अग्निः'),
		('रामः', '', 'प.8.4.22: रामः'),
		('सीता', '', 'प.8.4.22: सीता'),
	]

