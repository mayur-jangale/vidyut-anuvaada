# Sutra प.3.2.177: भ्राजभासधुर्विद्युतोर्जिपॄजुग्रावस्तुवः क्विप्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — BrAjaBAsaDurvidyutorjipFjugrAvastuvaH kvip

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.177"
SUTRA_TEXT = "भ्राजभासधुर्विद्युतोर्जिपॄजुग्रावस्तुवः क्विप्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — BrAjaBAsaDurvidyutorjipFjugrAvastuvaH kvip"


class Sutra32177:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

