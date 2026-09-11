# Sutra प.4.4.103: गुडादिभ्यष्ठञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — guqAdiByazWaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.103"
SUTRA_TEXT = "गुडादिभ्यष्ठञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — guqAdiByazWaY"


class Sutra44103:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.103: अग्निः'),
		('रामः', '', 'प.4.4.103: रामः'),
		('सीता', '', 'प.4.4.103: सीता'),
	]

