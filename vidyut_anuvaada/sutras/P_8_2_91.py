# Sutra प.8.2.91: ब्रूहिप्रेष्यश्रौषड्वौषडावहानामादेः
# (Final transformations (tripāḍī)) — brUhiprezyaSrOzaqvOzaqAvahAnAmAdeH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.91"
SUTRA_TEXT = "ब्रूहिप्रेष्यश्रौषड्वौषडावहानामादेः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — brUhiprezyaSrOzaqvOzaqAvahAnAmAdeH"


class Sutra8291:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.91: अग्निः'),
		('रामः', '', 'प.8.2.91: रामः'),
		('सीता', '', 'प.8.2.91: सीता'),
	]

