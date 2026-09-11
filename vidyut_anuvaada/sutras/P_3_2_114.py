# Sutra प.3.2.114: विभाषा साकाङ्क्षे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — viBAzA sAkANkze

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.114"
SUTRA_TEXT = "विभाषा साकाङ्क्षे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — viBAzA sAkANkze"


class Sutra32114:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

