# Sutra प.3.3.139: लिङ्निमित्ते लृङ् क्रियातिपत्तौ
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — liNnimitte lfN kriyAtipattO

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.139"
SUTRA_TEXT = "लिङ्निमित्ते लृङ् क्रियातिपत्तौ"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — liNnimitte lfN kriyAtipattO"


class Sutra33139:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

