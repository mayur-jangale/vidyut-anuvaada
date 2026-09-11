# Sutra प.8.2.47: श्योऽस्पर्शे
# (Final transformations (tripāḍī)) — Syo'sparSe

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.47"
SUTRA_TEXT = "श्योऽस्पर्शे"
SUTRA_DESC = "(Final transformations (tripāḍī)) — Syo'sparSe"


class Sutra8247:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.47: अग्निः'),
		('रामः', '', 'प.8.2.47: रामः'),
		('सीता', '', 'प.8.2.47: सीता'),
	]

