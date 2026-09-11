# Sutra प.4.3.75: ठगायस्थानेभ्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — WagAyasTAneByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.75"
SUTRA_TEXT = "ठगायस्थानेभ्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — WagAyasTAneByaH"


class Sutra4375:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.75: अग्निः'),
		('रामः', '', 'प.4.3.75: रामः'),
		('सीता', '', 'प.4.3.75: सीता'),
	]

