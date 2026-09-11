# Sutra प.4.1.120: स्त्रीभ्यो ढक्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.120"
SUTRA_TEXT = "स्त्रीभ्यो ढक्"
SUTRA_DESC = "supaḥ — continued"


class Sutra41120:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

