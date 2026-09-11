# Sutra प.7.4.36: दुरस्युर्द्रविणस्युर्वृषण्यतिरिषण्यति
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.36"
SUTRA_TEXT = "दुरस्युर्द्रविणस्युर्वृषण्यतिरिषण्यति"
SUTRA_DESC = "taddhita — continued"


class Sutra7436:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.36: अग्निः'),
		('रामः', '', 'प.7.4.36: रामः'),
		('सीता', '', 'प.7.4.36: सीता'),
	]

