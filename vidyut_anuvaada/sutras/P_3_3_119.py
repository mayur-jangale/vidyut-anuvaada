# Sutra प.3.3.119: गोचरसंचरवहव्रजव्यजापणनिगमाश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — gocarasaMcaravahavrajavyajApaRanigamASca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.119"
SUTRA_TEXT = "गोचरसंचरवहव्रजव्यजापणनिगमाश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — gocarasaMcaravahavrajavyajApaRanigamASca"


class Sutra33119:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

