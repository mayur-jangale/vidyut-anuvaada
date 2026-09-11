# Sutra प.3.3.72: ह्वः सम्प्रसारणं च न्यभ्युपविषु
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — hvaH samprasAraRaM ca nyaByupavizu

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.72"
SUTRA_TEXT = "ह्वः सम्प्रसारणं च न्यभ्युपविषु"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — hvaH samprasAraRaM ca nyaByupavizu"


class Sutra3372:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

