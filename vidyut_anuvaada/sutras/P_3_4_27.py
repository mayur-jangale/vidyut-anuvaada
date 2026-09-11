# Sutra प.3.4.27: अन्यथैवंकथमित्थंसु सिद्धाप्रयोगश्चेत्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — anyaTEvaMkaTamitTaMsu sidDAprayogaScet

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.27"
SUTRA_TEXT = "अन्यथैवंकथमित्थंसु सिद्धाप्रयोगश्चेत्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — anyaTEvaMkaTamitTaMsu sidDAprayogaScet"


class Sutra3427:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

