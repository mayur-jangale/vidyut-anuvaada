# Sutra प.3.4.47: उपदंशस्तृतीयायाम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — upadaMSastftIyAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.47"
SUTRA_TEXT = "उपदंशस्तृतीयायाम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — upadaMSastftIyAyAm"


class Sutra3447:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

