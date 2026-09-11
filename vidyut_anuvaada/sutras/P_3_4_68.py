# Sutra प.3.4.68: भव्यगेयप्रवचनीयोपस्थानीयजन्याप्लाव्यापात्या वा
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — BavyageyapravacanIyopasTAnIyajanyAplAvyApAtyA vA

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.68"
SUTRA_TEXT = "भव्यगेयप्रवचनीयोपस्थानीयजन्याप्लाव्यापात्या वा"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — BavyageyapravacanIyopasTAnIyajanyAplAvyApAtyA vA"


class Sutra3468:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

