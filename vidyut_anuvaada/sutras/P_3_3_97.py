# Sutra प.3.3.97: ऊतियूतिजूतिसातिहेतिकीर्तयश्च
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — UtiyUtijUtisAtihetikIrtayaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.97"
SUTRA_TEXT = "ऊतियूतिजूतिसातिहेतिकीर्तयश्च"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — UtiyUtijUtisAtihetikIrtayaSca"


class Sutra3397:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

