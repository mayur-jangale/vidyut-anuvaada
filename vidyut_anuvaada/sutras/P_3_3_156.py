# Sutra प.3.3.156: हेतुहेतुमतोर्लिङ्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — hetuhetumatorliN

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.156"
SUTRA_TEXT = "हेतुहेतुमतोर्लिङ्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — hetuhetumatorliN"


class Sutra33156:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

