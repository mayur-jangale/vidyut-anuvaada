# Sutra प.3.3.2: भूतेऽपि दृश्यन्ते
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — BUte'pi dfSyante

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.2"
SUTRA_TEXT = "भूतेऽपि दृश्यन्ते"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — BUte'pi dfSyante"


class Sutra332:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

