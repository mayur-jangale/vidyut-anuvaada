# Sutra प.3.2.109: उपेयिवाननाश्वाननूचानश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — upeyivAnanASvAnanUcAnaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.109"
SUTRA_TEXT = "उपेयिवाननाश्वाननूचानश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — upeyivAnanASvAnanUcAnaSca"


class Sutra32109:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

