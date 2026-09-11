# Sutra प.3.2.154: लषपतपदस्थाभूवृषहनकमगमशॄभ्य उकञ्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — lazapatapadasTABUvfzahanakamagamaSFBya ukaY

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.154"
SUTRA_TEXT = "लषपतपदस्थाभूवृषहनकमगमशॄभ्य उकञ्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — lazapatapadasTABUvfzahanakamagamaSFBya ukaY"


class Sutra32154:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

