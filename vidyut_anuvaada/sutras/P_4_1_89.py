# Sutra प.4.1.89: गोत्रेऽलुगचि
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.89"
SUTRA_TEXT = "गोत्रेऽलुगचि"
SUTRA_DESC = "supaḥ — continued"


class Sutra4189:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

