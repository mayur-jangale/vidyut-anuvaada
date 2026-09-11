# Sutra प.8.1.52: लोट् च
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.52"
SUTRA_TEXT = "लोट् च"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8152:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.52: अग्निः'),
		('रामः', '', 'प.8.1.52: रामः'),
		('सीता', '', 'प.8.1.52: सीता'),
	]

