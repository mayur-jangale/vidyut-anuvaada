# Sutra प.4.1.46: नित्यं छन्दसि
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.46"
SUTRA_TEXT = "नित्यं छन्दसि"
SUTRA_DESC = "supaḥ — continued"


class Sutra4146:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

