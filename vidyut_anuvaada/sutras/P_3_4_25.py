# Sutra प.3.4.25: कर्मण्याक्रोशे कृञः खमुञ्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — karmaRyAkroSe kfYaH KamuY

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.25"
SUTRA_TEXT = "कर्मण्याक्रोशे कृञः खमुञ्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — karmaRyAkroSe kfYaH KamuY"


class Sutra3425:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

