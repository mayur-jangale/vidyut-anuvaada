# Sutra प.4.2.56: संग्रामे प्रयोजनयोद्धृभ्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — saMgrAme prayojanayodDfByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.56"
SUTRA_TEXT = "संग्रामे प्रयोजनयोद्धृभ्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — saMgrAme prayojanayodDfByaH"


class Sutra4256:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.56: अग्निः'),
		('रामः', '', 'प.4.2.56: रामः'),
		('सीता', '', 'प.4.2.56: सीता'),
	]

