# Sutra प.8.2.55: अनुपसर्गात् फुल्लक्षीबकृशोल्लाघाः
# (Final transformations (tripāḍī)) — anupasargAt PullakzIbakfSollAGAH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.55"
SUTRA_TEXT = "अनुपसर्गात् फुल्लक्षीबकृशोल्लाघाः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — anupasargAt PullakzIbakfSollAGAH"


class Sutra8255:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.55: अग्निः'),
		('रामः', '', 'प.8.2.55: रामः'),
		('सीता', '', 'प.8.2.55: सीता'),
	]

