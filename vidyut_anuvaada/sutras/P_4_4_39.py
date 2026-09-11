# Sutra प.4.4.39: पदोत्तरपदं गृह्णाति
# (Sup-sthāna (nominal endings) and kṛt-affixes) — padottarapadaM gfhRAti

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.39"
SUTRA_TEXT = "पदोत्तरपदं गृह्णाति"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — padottarapadaM gfhRAti"


class Sutra4439:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.39: अग्निः'),
		('रामः', '', 'प.4.4.39: रामः'),
		('सीता', '', 'प.4.4.39: सीता'),
	]

