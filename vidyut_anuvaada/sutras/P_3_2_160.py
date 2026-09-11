# Sutra प.3.2.160: सृघस्यदः क्मरच्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — sfGasyadaH kmarac

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.160"
SUTRA_TEXT = "सृघस्यदः क्मरच्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — sfGasyadaH kmarac"


class Sutra32160:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

