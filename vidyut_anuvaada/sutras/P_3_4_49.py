# Sutra प.3.4.49: सप्तम्यां चोपपीडरुधकर्षः
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — saptamyAM copapIqaruDakarzaH

from sutra_engines import apply_general

SUTRA_CODE = "प.3.4.49"
SUTRA_TEXT = "सप्तम्यां चोपपीडरुधकर्षः"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — saptamyAM copapIqaruDakarzaH"


class Sutra3449:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

