# Sutra प.3.2.139: ग्लाजिस्थश्च क्स्नुः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — glAjisTaSca ksnuH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.139"
SUTRA_TEXT = "ग्लाजिस्थश्च क्स्नुः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — glAjisTaSca ksnuH"


class Sutra32139:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

