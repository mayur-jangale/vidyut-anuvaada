# Sutra प.3.3.110: विभाषाऽऽख्यानपरिप्रश्नयोरिञ् च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — viBAzA''KyAnaparipraSnayoriY ca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.110"
SUTRA_TEXT = "विभाषाऽऽख्यानपरिप्रश्नयोरिञ् च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — viBAzA''KyAnaparipraSnayoriY ca"


class Sutra33110:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

