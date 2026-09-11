# Sutra प.4.1.117: विकर्णशुङ्गच्छगलाद्वत्सभरद्वाजात्रिषु
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.117"
SUTRA_TEXT = "विकर्णशुङ्गच्छगलाद्वत्सभरद्वाजात्रिषु"
SUTRA_DESC = "supaḥ — continued"


class Sutra41117:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

