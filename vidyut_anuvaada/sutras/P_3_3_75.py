# Sutra प.3.3.75: भावेऽनुपसर्गस्य
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — BAve'nupasargasya

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.75"
SUTRA_TEXT = "भावेऽनुपसर्गस्य"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — BAve'nupasargasya"


class Sutra3375:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

