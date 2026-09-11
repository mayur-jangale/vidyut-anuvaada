# Sutra प.3.4.64: अन्वच्यानुलोम्ये
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — anvacyAnulomye

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.64"
SUTRA_TEXT = "अन्वच्यानुलोम्ये"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — anvacyAnulomye"


class Sutra3464:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

