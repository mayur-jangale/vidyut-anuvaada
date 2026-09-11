# Sutra प.4.1.14: अनुपसर्जनात्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.14"
SUTRA_TEXT = "अनुपसर्जनात्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4114:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

