# Sutra प.6.3.111: ढ्रलोपे पूर्वस्य दीर्घोऽणः
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.111"
SUTRA_TEXT = "ढ्रलोपे पूर्वस्य दीर्घोऽणः"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63111:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.111: अग्निः'),
		('रामः', '', 'प.6.3.111: रामः'),
		('सीता', '', 'प.6.3.111: सीता'),
	]

