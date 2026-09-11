# Sutra प.3.2.162: विदिभिदिच्छिदेः कुरच्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — vidiBidicCideH kurac

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.162"
SUTRA_TEXT = "विदिभिदिच्छिदेः कुरच्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — vidiBidicCideH kurac"


class Sutra32162:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

