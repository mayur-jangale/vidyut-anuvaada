# Sutra प.3.3.24: श्रिणीभुवोऽनुपसर्गे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — SriRIBuvo'nupasarge

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.24"
SUTRA_TEXT = "श्रिणीभुवोऽनुपसर्गे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — SriRIBuvo'nupasarge"


class Sutra3324:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

