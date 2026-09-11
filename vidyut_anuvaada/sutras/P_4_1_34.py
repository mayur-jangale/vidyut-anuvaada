# Sutra प.4.1.34: विभाषा सपूर्वस्य
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.34"
SUTRA_TEXT = "विभाषा सपूर्वस्य"
SUTRA_DESC = "supaḥ — continued"


class Sutra4134:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

