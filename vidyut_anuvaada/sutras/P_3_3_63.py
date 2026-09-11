# Sutra प.3.3.63: यमः समुपनिविषु च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — yamaH samupanivizu ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.63"
SUTRA_TEXT = "यमः समुपनिविषु च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — yamaH samupanivizu ca"


class Sutra3363:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

