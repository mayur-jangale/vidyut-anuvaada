# Sutra प.3.4.57: अस्यतितृषोः क्रियाऽन्तरे कालेषु
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — asyatitfzoH kriyA'ntare kAlezu

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.57"
SUTRA_TEXT = "अस्यतितृषोः क्रियाऽन्तरे कालेषु"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — asyatitfzoH kriyA'ntare kAlezu"


class Sutra3457:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

