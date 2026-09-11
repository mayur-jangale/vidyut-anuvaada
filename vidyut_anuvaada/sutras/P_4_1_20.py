# Sutra प.4.1.20: वयसि प्रथमे
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.20"
SUTRA_TEXT = "वयसि प्रथमे"
SUTRA_DESC = "supaḥ — continued"


class Sutra4120:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

