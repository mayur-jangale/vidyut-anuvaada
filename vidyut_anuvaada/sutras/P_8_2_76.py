# Sutra प.8.2.76: र्वोरुपधाया दीर्घ इकः
# (Final transformations (tripāḍī)) — rvorupaDAyA dIrGa ikaH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.76"
SUTRA_TEXT = "र्वोरुपधाया दीर्घ इकः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — rvorupaDAyA dIrGa ikaH"


class Sutra8276:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.76: अग्निः'),
		('रामः', '', 'प.8.2.76: रामः'),
		('सीता', '', 'प.8.2.76: सीता'),
	]

