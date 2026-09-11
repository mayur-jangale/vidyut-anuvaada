# Sutra प.1.4.39: राधीक्ष्योर्यस्य विप्रश्नः
# (Samjna (technical definitions)) — rADIkzyoryasya vipraSnaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.39"
SUTRA_TEXT = "राधीक्ष्योर्यस्य विप्रश्नः"
SUTRA_DESC = "(Samjna (technical definitions)) — rADIkzyoryasya vipraSnaH"


class Sutra1439:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_39
		return apply_1_4_39(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-vipraSna-sampradAnam:अग्निः'),
		('रामः', '', 'not-vipraSna-sampradAnam:रामः'),
		('सीता', '', 'not-vipraSna-sampradAnam:सीता'),
	]

