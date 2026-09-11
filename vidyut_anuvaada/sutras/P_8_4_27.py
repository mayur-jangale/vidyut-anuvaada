# Sutra प.8.4.27: नश्च धातुस्थोरुषुभ्यः
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.27"
SUTRA_TEXT = "नश्च धातुस्थोरुषुभ्यः"
SUTRA_DESC = "final transformations — continued"


class Sutra8427:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.27: अग्निः'),
		('रामः', '', 'प.8.4.27: रामः'),
		('सीता', '', 'प.8.4.27: सीता'),
	]

