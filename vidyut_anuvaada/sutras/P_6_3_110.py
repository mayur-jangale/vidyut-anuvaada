# Sutra प.6.3.110: संख्याविसायपूर्वस्याह्नस्याहन्नन्यतरस्यां ङौ
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.110"
SUTRA_TEXT = "संख्याविसायपूर्वस्याह्नस्याहन्नन्यतरस्यां ङौ"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63110:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.110: अग्निः'),
		('रामः', '', 'प.6.3.110: रामः'),
		('सीता', '', 'प.6.3.110: सीता'),
	]

