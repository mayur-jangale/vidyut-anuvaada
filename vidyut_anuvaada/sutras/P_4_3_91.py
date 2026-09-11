# Sutra प.4.3.91: आयुधजीविभ्यश्छः पर्वते
# (Sup-sthāna (nominal endings) and kṛt-affixes) — AyuDajIviByaSCaH parvate

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.91"
SUTRA_TEXT = "आयुधजीविभ्यश्छः पर्वते"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — AyuDajIviByaSCaH parvate"


class Sutra4391:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.91: अग्निः'),
		('रामः', '', 'प.4.3.91: रामः'),
		('सीता', '', 'प.4.3.91: सीता'),
	]

