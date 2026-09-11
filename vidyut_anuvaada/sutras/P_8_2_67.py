# Sutra प.8.2.67: अवयाःश्वेतवाःपुरोडाश्च
# (Final transformations (tripāḍī)) — avayAHSvetavAHpuroqASca

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.67"
SUTRA_TEXT = "अवयाःश्वेतवाःपुरोडाश्च"
SUTRA_DESC = "(Final transformations (tripāḍī)) — avayAHSvetavAHpuroqASca"


class Sutra8267:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.67: अग्निः'),
		('रामः', '', 'प.8.2.67: रामः'),
		('सीता', '', 'प.8.2.67: सीता'),
	]

