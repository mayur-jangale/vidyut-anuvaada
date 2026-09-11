# Sutra प.3.2.141: शमित्यष्टाभ्यो घिनुण्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — SamityazwAByo GinuR

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.141"
SUTRA_TEXT = "शमित्यष्टाभ्यो घिनुण्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — SamityazwAByo GinuR"


class Sutra32141:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

