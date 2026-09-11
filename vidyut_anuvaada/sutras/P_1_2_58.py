# Sutra प.1.2.58: जात्याख्यायामेकस्मिन् बहुवचनमन्यतरस्याम्
# (Samjna (technical definitions)) — jAtyAKyAyAmekasmin bahuvacanamanyatarasyAm

from P_1_2 import apply_1_2_58

SUTRA_CODE = "प.1.2.58"
SUTRA_TEXT = "जात्याख्यायामेकस्मिन् बहुवचनमन्यतरस्याम्"
SUTRA_DESC = "(Samjna (technical definitions)) — jAtyAKyAyAmekasmin bahuvacanamanyatarasyAm"


class Sutra1258:
	def apply(self, word, pos):
		return apply_1_2_58(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-jāti:अग्निः'),
		('रामः', '', 'non-jāti:रामः'),
		('सीता', '', 'non-jāti:सीता'),
	]

