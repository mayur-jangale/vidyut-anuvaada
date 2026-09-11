# Sutra प.1.4.44: परिक्रयणे सम्प्रदानमन्यतरस्याम्
# (Samjna (technical definitions)) — parikrayaRe sampradAnamanyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.44"
SUTRA_TEXT = "परिक्रयणे सम्प्रदानमन्यतरस्याम्"
SUTRA_DESC = "(Samjna (technical definitions)) — parikrayaRe sampradAnamanyatarasyAm"


class Sutra1444:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_44
		return apply_1_4_44(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-optional-sampradAnam:अग्निः'),
		('रामः', '', 'not-optional-sampradAnam:रामः'),
		('सीता', '', 'not-optional-sampradAnam:सीता'),
	]

