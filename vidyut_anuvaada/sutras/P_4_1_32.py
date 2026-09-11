# Sutra प.4.1.32: अन्तर्वत्पतिवतोर्नुक्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.32"
SUTRA_TEXT = "अन्तर्वत्पतिवतोर्नुक्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4132:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

