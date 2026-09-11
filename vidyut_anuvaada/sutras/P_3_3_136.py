# Sutra प.3.3.136: भविष्यति मर्यादावचनेऽवरस्मिन्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — Bavizyati maryAdAvacane'varasmin

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.136"
SUTRA_TEXT = "भविष्यति मर्यादावचनेऽवरस्मिन्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — Bavizyati maryAdAvacane'varasmin"


class Sutra33136:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

