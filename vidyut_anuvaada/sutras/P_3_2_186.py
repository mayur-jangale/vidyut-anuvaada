# Sutra प.3.2.186: कर्तरि चर्षिदेवतयोः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kartari carzidevatayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.186"
SUTRA_TEXT = "कर्तरि चर्षिदेवतयोः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kartari carzidevatayoH"


class Sutra32186:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

