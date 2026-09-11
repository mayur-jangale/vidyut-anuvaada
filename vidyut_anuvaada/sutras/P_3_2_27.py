# Sutra प.3.2.27: छन्दसि वनसनरक्षिमथाम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — Candasi vanasanarakzimaTAm

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.27"
SUTRA_TEXT = "छन्दसि वनसनरक्षिमथाम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — Candasi vanasanarakzimaTAm"


class Sutra3227:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

