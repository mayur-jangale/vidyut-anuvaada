# Sutra प.4.1.105: गर्गादिभ्यो यञ्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.105"
SUTRA_TEXT = "गर्गादिभ्यो यञ्"
SUTRA_DESC = "supaḥ — continued"


class Sutra41105:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

