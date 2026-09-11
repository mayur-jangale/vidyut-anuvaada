# Sutra प.4.1.144: भ्रातुर्व्यच्च
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.144"
SUTRA_TEXT = "भ्रातुर्व्यच्च"
SUTRA_DESC = "supaḥ — continued"


class Sutra41144:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

