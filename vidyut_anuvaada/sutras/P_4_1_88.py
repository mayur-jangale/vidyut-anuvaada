# Sutra प.4.1.88: द्विगोर्लुगनपत्ये
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.88"
SUTRA_TEXT = "द्विगोर्लुगनपत्ये"
SUTRA_DESC = "supaḥ — continued"


class Sutra4188:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

