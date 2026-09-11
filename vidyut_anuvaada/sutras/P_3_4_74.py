# Sutra प.3.4.74: भीमादयोऽपादाने
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — BImAdayo'pAdAne

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.74"
SUTRA_TEXT = "भीमादयोऽपादाने"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — BImAdayo'pAdAne"


class Sutra3474:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

