# Sutra प.6.3.60: मन्थौदनसक्तुबिन्दुवज्रभारहारवीवधगाहेषु च
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.60"
SUTRA_TEXT = "मन्थौदनसक्तुबिन्दुवज्रभारहारवीवधगाहेषु च"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6360:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.60: अग्निः'),
		('रामः', '', 'प.6.3.60: रामः'),
		('सीता', '', 'प.6.3.60: सीता'),
	]

