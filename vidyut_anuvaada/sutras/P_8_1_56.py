# Sutra प.8.1.56: यद्धितुपरं छन्दसि
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.56"
SUTRA_TEXT = "यद्धितुपरं छन्दसि"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8156:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.56: अग्निः'),
		('रामः', '', 'प.8.1.56: रामः'),
		('सीता', '', 'प.8.1.56: सीता'),
	]

