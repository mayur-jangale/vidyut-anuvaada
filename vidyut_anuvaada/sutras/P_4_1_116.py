# Sutra प.4.1.116: कन्यायाः कनीन च
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.116"
SUTRA_TEXT = "कन्यायाः कनीन च"
SUTRA_DESC = "supaḥ — continued"


class Sutra41116:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

