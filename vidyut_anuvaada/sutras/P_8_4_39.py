# Sutra प.8.4.39: क्षुभ्नाऽऽदिषु च
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.39"
SUTRA_TEXT = "क्षुभ्नाऽऽदिषु च"
SUTRA_DESC = "final transformations — continued"


class Sutra8439:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.39: अग्निः'),
		('रामः', '', 'प.8.4.39: रामः'),
		('सीता', '', 'प.8.4.39: सीता'),
	]

