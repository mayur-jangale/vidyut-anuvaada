# Sutra प.3.3.163: प्रैषातिसर्गप्राप्तकालेषु कृत्याश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — prEzAtisargaprAptakAlezu kftyASca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.163"
SUTRA_TEXT = "प्रैषातिसर्गप्राप्तकालेषु कृत्याश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — prEzAtisargaprAptakAlezu kftyASca"


class Sutra33163:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

