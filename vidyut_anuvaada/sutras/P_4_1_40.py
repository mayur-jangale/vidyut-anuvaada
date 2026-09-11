# Sutra प.4.1.40: अन्यतो ङीष्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.40"
SUTRA_TEXT = "अन्यतो ङीष्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4140:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

