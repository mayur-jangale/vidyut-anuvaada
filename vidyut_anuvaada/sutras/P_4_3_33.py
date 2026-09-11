# Sutra प.4.3.33: अणञौ च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — aRaYO ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.33"
SUTRA_TEXT = "अणञौ च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — aRaYO ca"


class Sutra4333:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.33: अग्निः'),
		('रामः', '', 'प.4.3.33: रामः'),
		('सीता', '', 'प.4.3.33: सीता'),
	]

