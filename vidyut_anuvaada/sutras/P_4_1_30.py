# Sutra प.4.1.30: केवलमामकभागधेयपापापरसमानार्यकृत-सुमङ्गलभेषजाच्च
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.30"
SUTRA_TEXT = "केवलमामकभागधेयपापापरसमानार्यकृत-सुमङ्गलभेषजाच्च"
SUTRA_DESC = "supaḥ — continued"


class Sutra4130:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

