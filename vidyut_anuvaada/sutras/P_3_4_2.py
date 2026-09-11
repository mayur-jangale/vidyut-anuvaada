# Sutra प.3.4.2: क्रियासमभिहारे लोट्; लोटो हिस्वौ; वा च तध्वमोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kriyAsamaBihAre low; lowo hisvO; vA ca taDvamoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.2"
SUTRA_TEXT = "क्रियासमभिहारे लोट्; लोटो हिस्वौ; वा च तध्वमोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kriyAsamaBihAre low; lowo hisvO; vA ca taDvamoH"


class Sutra342:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

