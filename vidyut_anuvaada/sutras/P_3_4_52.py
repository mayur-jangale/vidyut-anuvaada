# Sutra प.3.4.52: अपादाने परीप्सायाम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — apAdAne parIpsAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.52"
SUTRA_TEXT = "अपादाने परीप्सायाम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — apAdAne parIpsAyAm"


class Sutra3452:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

