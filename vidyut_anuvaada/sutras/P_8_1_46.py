# Sutra प.8.1.46: एहिमन्ये प्रहासे लृट्
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.46"
SUTRA_TEXT = "एहिमन्ये प्रहासे लृट्"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8146:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.46: अग्निः'),
		('रामः', '', 'प.8.1.46: रामः'),
		('सीता', '', 'प.8.1.46: सीता'),
	]

