# Sutra प.3.2.26: फलेग्रहिरात्मम्भरिश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — PalegrahirAtmamBariSca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.26"
SUTRA_TEXT = "फलेग्रहिरात्मम्भरिश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — PalegrahirAtmamBariSca"


class Sutra3226:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

