# Sutra प.8.2.74: सिपि धातो रुर्वा
# (Final transformations (tripāḍī)) — sipi DAto rurvA

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.74"
SUTRA_TEXT = "सिपि धातो रुर्वा"
SUTRA_DESC = "(Final transformations (tripāḍī)) — sipi DAto rurvA"


class Sutra8274:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.74: अग्निः'),
		('रामः', '', 'प.8.2.74: रामः'),
		('सीता', '', 'प.8.2.74: सीता'),
	]

