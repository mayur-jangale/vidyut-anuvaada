# Sutra प.4.1.85: दित्यदित्यादित्यपत्युत्तरपदाण्ण्यः
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.85"
SUTRA_TEXT = "दित्यदित्यादित्यपत्युत्तरपदाण्ण्यः"
SUTRA_DESC = "supaḥ — continued"


class Sutra4185:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

