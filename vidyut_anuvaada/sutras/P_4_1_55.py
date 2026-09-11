# Sutra प.4.1.55: नासिकोदरौष्ठजङ्घादन्तकर्णशृङ्गाच्च
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.55"
SUTRA_TEXT = "नासिकोदरौष्ठजङ्घादन्तकर्णशृङ्गाच्च"
SUTRA_DESC = "supaḥ — continued"


class Sutra4155:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

