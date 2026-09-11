# Sutra प.4.1.87: स्त्रीपुंसाभ्यां नञ्स्नञौ भवनात्
# supaḥ — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.4.1.87"
SUTRA_TEXT = "स्त्रीपुंसाभ्यां नञ्स्नञौ भवनात्"
SUTRA_DESC = "supaḥ — continued"


class Sutra4187:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
		("अग्निः", "", apply_general("अग्निः", "", SUTRA_CODE)),
	]

