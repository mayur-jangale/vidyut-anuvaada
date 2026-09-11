# Sutra प.4.1.96: बाह्वादिभ्यश्च
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.96"
SUTRA_TEXT = "बाह्वादिभ्यश्च"
SUTRA_DESC = "supaḥ — continued"


class Sutra4196:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

