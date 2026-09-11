# Sutra प.7.2.117: तद्धितेष्वचामादेः
# (Taddhita (secondary derivations)) — tadDitezvacAmAdeH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.117"
SUTRA_TEXT = "तद्धितेष्वचामादेः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — tadDitezvacAmAdeH"


class Sutra72117:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.117: अग्निः'),
		('रामः', '', 'प.7.2.117: रामः'),
		('सीता', '', 'प.7.2.117: सीता'),
	]

