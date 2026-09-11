# Sutra प.8.2.71: भुवश्च महाव्याहृतेः
# (Final transformations (tripāḍī)) — BuvaSca mahAvyAhfteH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.71"
SUTRA_TEXT = "भुवश्च महाव्याहृतेः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — BuvaSca mahAvyAhfteH"


class Sutra8271:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.71: अग्निः'),
		('रामः', '', 'प.8.2.71: रामः'),
		('सीता', '', 'प.8.2.71: सीता'),
	]

