# Sutra प.3.3.130: अन्येभ्योऽपि दृश्यते
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — anyeByo'pi dfSyate

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.130"
SUTRA_TEXT = "अन्येभ्योऽपि दृश्यते"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — anyeByo'pi dfSyate"


class Sutra33130:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

