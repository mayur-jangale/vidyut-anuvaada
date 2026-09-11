# Sutra प.3.4.96: वैतोऽन्यत्र
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — vEto'nyatra

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.96"
SUTRA_TEXT = "वैतोऽन्यत्र"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — vEto'nyatra"


class Sutra3496:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

