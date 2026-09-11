# Sutra प.3.2.126: लक्षणहेत्वोः क्रियायाः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — lakzaRahetvoH kriyAyAH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.126"
SUTRA_TEXT = "लक्षणहेत्वोः क्रियायाः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — lakzaRahetvoH kriyAyAH"


class Sutra32126:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

