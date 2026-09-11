# Sutra प.3.4.95: आत ऐ
# ekāj anāṅ gatirliṅaḥ — single non-ṅ suffix in liṅ takes specific path

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.95"
SUTRA_TEXT = "आत ऐ"
SUTRA_DESC = "ekāj anāṅ gatirliṅaḥ — single non-ṅ suffix in liṅ takes specific path"


class Sutra3495:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

