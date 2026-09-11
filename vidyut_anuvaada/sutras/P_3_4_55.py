# Sutra प.3.4.55: परिक्लिश्यमाने च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — parikliSyamAne ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.55"
SUTRA_TEXT = "परिक्लिश्यमाने च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — parikliSyamAne ca"


class Sutra3455:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

