# Sutra प.4.1.95: अत इञ्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.95"
SUTRA_TEXT = "अत इञ्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4195:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

