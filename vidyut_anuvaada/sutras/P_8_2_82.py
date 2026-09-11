# Sutra प.8.2.82: वाक्यस्य टेः प्लुत उदात्तः
# (Final transformations (tripāḍī)) — vAkyasya weH pluta udAttaH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.82"
SUTRA_TEXT = "वाक्यस्य टेः प्लुत उदात्तः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — vAkyasya weH pluta udAttaH"


class Sutra8282:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.82: अग्निः'),
		('रामः', '', 'प.8.2.82: रामः'),
		('सीता', '', 'प.8.2.82: सीता'),
	]

