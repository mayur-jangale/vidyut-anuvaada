# Sutra प.3.3.40: हस्तादाने चेरस्तेये
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — hastAdAne cerasteye

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.40"
SUTRA_TEXT = "हस्तादाने चेरस्तेये"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — hastAdAne cerasteye"


class Sutra3340:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

