# Sutra प.4.1.56: न क्रोडादिबह्वचः
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.56"
SUTRA_TEXT = "न क्रोडादिबह्वचः"
SUTRA_DESC = "supaḥ — continued"


class Sutra4156:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

