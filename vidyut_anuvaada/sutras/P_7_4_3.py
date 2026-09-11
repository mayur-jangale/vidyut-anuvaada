# Sutra प.7.4.3: भ्राजभासभाषदीपजीवमीलपीडामन्यतरस्याम्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.3"
SUTRA_TEXT = "भ्राजभासभाषदीपजीवमीलपीडामन्यतरस्याम्"
SUTRA_DESC = "taddhita — continued"


class Sutra743:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.3: अग्निः'),
		('रामः', '', 'प.7.4.3: रामः'),
		('सीता', '', 'प.7.4.3: सीता'),
	]

