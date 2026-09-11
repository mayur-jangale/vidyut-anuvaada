# Sutra प.8.2.42: रदाभ्यां निष्ठातो नः पूर्वस्य च दः
# (Final transformations (tripāḍī)) — radAByAM nizWAto naH pUrvasya ca daH

from sutra_engines import apply_general

SUTRA_CODE = "प.8.2.42"
SUTRA_TEXT = "रदाभ्यां निष्ठातो नः पूर्वस्य च दः"
SUTRA_DESC = "(Final transformations (tripāḍī)) — radAByAM nizWAto naH pUrvasya ca daH"


class Sutra8242:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.2.42: अग्निः'),
		('रामः', '', 'प.8.2.42: रामः'),
		('सीता', '', 'प.8.2.42: सीता'),
	]

