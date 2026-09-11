# Sutra प.6.2.2: तत्पुरुषे तुल्यार्थतृतीयासप्तम्युपमानाव्ययद्वितीयाकृत्याः
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.2"
SUTRA_TEXT = "तत्पुरुषे तुल्यार्थतृतीयासप्तम्युपमानाव्ययद्वितीयाकृत्याः"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra622:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.2: अग्निः'),
		('रामः', '', 'प.6.2.2: रामः'),
		('सीता', '', 'प.6.2.2: सीता'),
	]

