# Sutra प.3.4.62: नाधाऽर्थप्रत्यये च्व्यर्थे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — nADA'rTapratyaye cvyarTe

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.62"
SUTRA_TEXT = "नाधाऽर्थप्रत्यये च्व्यर्थे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — nADA'rTapratyaye cvyarTe"


class Sutra3462:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

