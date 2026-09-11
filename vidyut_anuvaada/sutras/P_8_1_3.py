# Sutra प.8.1.3: अनुदात्तं च
# naścāpadāntasya ṅiḥ — न् becomes ङ् before ङि-ending suffixes

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.3"
SUTRA_TEXT = "अनुदात्तं च"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — न् becomes ङ् before ङि-ending suffixes"


class Sutra813:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.3: अग्निः'),
		('रामः', '', 'प.8.1.3: रामः'),
		('सीता', '', 'प.8.1.3: सीता'),
	]

