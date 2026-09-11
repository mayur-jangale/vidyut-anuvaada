# Sutra प.3.2.64: वहश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — vahaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.64"
SUTRA_TEXT = "वहश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — vahaSca"


class Sutra3264:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

