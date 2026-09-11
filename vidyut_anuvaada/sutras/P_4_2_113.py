# Sutra प.4.2.113: न द्व्यचः प्राच्यभरतेषु
# (Sup-sthāna (nominal endings) and kṛt-affixes) — na dvyacaH prAcyaBaratezu

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.113"
SUTRA_TEXT = "न द्व्यचः प्राच्यभरतेषु"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — na dvyacaH prAcyaBaratezu"


class Sutra42113:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.113: अग्निः'),
		('रामः', '', 'प.4.2.113: रामः'),
		('सीता', '', 'प.4.2.113: सीता'),
	]

