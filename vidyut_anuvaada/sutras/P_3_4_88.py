# Sutra प.3.4.88: वा छन्दसि
# luṅ — aorist endings

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.88"
SUTRA_TEXT = "वा छन्दसि"
SUTRA_DESC = "luṅ — aorist endings"


class Sutra3488:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

