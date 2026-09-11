# Sutra प.4.3.43: कालात् साधुपुष्प्यत्पच्यमानेषु
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kAlAt sADupuzpyatpacyamAnezu

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.43"
SUTRA_TEXT = "कालात् साधुपुष्प्यत्पच्यमानेषु"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kAlAt sADupuzpyatpacyamAnezu"


class Sutra4343:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.43: अग्निः'),
		('रामः', '', 'प.4.3.43: रामः'),
		('सीता', '', 'प.4.3.43: सीता'),
	]

