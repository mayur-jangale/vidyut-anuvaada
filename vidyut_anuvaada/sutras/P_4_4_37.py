# Sutra प.4.4.37: माथोत्तरपदपदव्यनुपदं धावति
# (Sup-sthāna (nominal endings) and kṛt-affixes) — mATottarapadapadavyanupadaM DAvati

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.37"
SUTRA_TEXT = "माथोत्तरपदपदव्यनुपदं धावति"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — mATottarapadapadavyanupadaM DAvati"


class Sutra4437:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.37: अग्निः'),
		('रामः', '', 'प.4.4.37: रामः'),
		('सीता', '', 'प.4.4.37: सीता'),
	]

