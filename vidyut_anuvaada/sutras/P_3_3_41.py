# Sutra प.3.3.41: निवासचितिशरीरोपसमाधानेष्वादेश्च कः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — nivAsacitiSarIropasamADAnezvAdeSca kaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.41"
SUTRA_TEXT = "निवासचितिशरीरोपसमाधानेष्वादेश्च कः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — nivAsacitiSarIropasamADAnezvAdeSca kaH"


class Sutra3341:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

