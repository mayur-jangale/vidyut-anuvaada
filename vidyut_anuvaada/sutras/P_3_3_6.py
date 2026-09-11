# Sutra प.3.3.6: किंवृत्ते लिप्सायाम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kiMvftte lipsAyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.6"
SUTRA_TEXT = "किंवृत्ते लिप्सायाम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kiMvftte lipsAyAm"


class Sutra336:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

