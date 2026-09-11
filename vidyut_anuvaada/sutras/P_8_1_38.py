# Sutra प.8.1.38: उपसर्गव्यपेतं च
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.38"
SUTRA_TEXT = "उपसर्गव्यपेतं च"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8138:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.38: अग्निः'),
		('रामः', '', 'प.8.1.38: रामः'),
		('सीता', '', 'प.8.1.38: सीता'),
	]

