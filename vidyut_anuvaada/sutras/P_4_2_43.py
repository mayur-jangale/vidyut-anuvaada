# Sutra प.4.2.43: ग्रामजनबन्धुसहायेभ्यः तल्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — grAmajanabanDusahAyeByaH tal

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.43"
SUTRA_TEXT = "ग्रामजनबन्धुसहायेभ्यः तल्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — grAmajanabanDusahAyeByaH tal"


class Sutra4243:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.43: अग्निः'),
		('रामः', '', 'प.4.2.43: रामः'),
		('सीता', '', 'प.4.2.43: सीता'),
	]

