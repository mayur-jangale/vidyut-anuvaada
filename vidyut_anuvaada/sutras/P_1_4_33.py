# Sutra प.1.4.33: रुच्यर्थानां प्रीयमाणः
# (Samjna (technical definitions)) — rucyarTAnAM prIyamARaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.33"
SUTRA_TEXT = "रुच्यर्थानां प्रीयमाणः"
SUTRA_DESC = "(Samjna (technical definitions)) — rucyarTAnAM prIyamARaH"


class Sutra1433:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_33
		return apply_1_4_33(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-ruci-sampradAnam:अग्निः'),
		('रामः', '', 'not-ruci-sampradAnam:रामः'),
		('सीता', '', 'not-ruci-sampradAnam:सीता'),
	]

