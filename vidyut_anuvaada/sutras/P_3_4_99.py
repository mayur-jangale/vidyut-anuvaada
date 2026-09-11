# Sutra प.3.4.99: नित्यं ङितः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — nityaM NitaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.99"
SUTRA_TEXT = "नित्यं ङितः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — nityaM NitaH"


class Sutra3499:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

