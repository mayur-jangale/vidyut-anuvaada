# Sutra प.1.4.24: ध्रुवमपायेऽपादानम्
# (Samjna (technical definitions)) — DruvamapAye'pAdAnam

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.24"
SUTRA_TEXT = "ध्रुवमपायेऽपादानम्"
SUTRA_DESC = "(Samjna (technical definitions)) — DruvamapAye'pAdAnam"


class Sutra1424:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_24
		return apply_1_4_24(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-apadana:अग्निः'),
		('रामः', '', 'not-apadana:रामः'),
		('सीता', '', 'not-apadana:सीता'),
	]

