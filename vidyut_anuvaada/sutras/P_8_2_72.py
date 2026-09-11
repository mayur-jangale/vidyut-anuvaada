# Sutra प.8.2.72: वसुस्रंसुध्वंस्वनडुहां दः
# (Final transformations (tripāḍī)) — vasusraMsuDvaMsvanaquhAM daH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.72"
SUTRA_TEXT = "वसुस्रंसुध्वंस्वनडुहां दः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — vasusraMsuDvaMsvanaquhAM daH"


class Sutra8272:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.72: अग्निः'),
		('रामः', '', 'प.8.2.72: रामः'),
		('सीता', '', 'प.8.2.72: सीता'),
	]

