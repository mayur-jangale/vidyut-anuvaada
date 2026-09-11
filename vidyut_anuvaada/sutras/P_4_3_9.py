# Sutra प.4.3.9: अ साम्प्रतिके
# (Sup-sthāna (nominal endings) and kṛt-affixes) — a sAmpratike

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.9"
SUTRA_TEXT = "अ साम्प्रतिके"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — a sAmpratike"


class Sutra439:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.9: अग्निः'),
		('रामः', '', 'प.4.3.9: रामः'),
		('सीता', '', 'प.4.3.9: सीता'),
	]

