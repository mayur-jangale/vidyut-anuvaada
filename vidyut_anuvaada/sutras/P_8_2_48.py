# Sutra प.8.2.48: अञ्चोऽनपादाने
# (Final transformations (tripāḍī)) — aYco'napAdAne

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.48"
SUTRA_TEXT = "अञ्चोऽनपादाने"
SUTRA_DESC = "(Final transformations (tripāḍī)) — aYco'napAdAne"


class Sutra8248:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.48: अग्निः'),
		('रामः', '', 'प.8.2.48: रामः'),
		('सीता', '', 'प.8.2.48: सीता'),
	]

