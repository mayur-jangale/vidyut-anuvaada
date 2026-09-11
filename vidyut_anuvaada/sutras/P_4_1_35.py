# Sutra प.4.1.35: नित्यं सपत्न्यादिषु
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.35"
SUTRA_TEXT = "नित्यं सपत्न्यादिषु"
SUTRA_DESC = "supaḥ — continued"


class Sutra4135:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

