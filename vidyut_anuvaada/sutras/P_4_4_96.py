# Sutra प.4.4.96: बन्धने चर्षौ
# (Sup-sthāna (nominal endings) and kṛt-affixes) — banDane carzO

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.96"
SUTRA_TEXT = "बन्धने चर्षौ"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — banDane carzO"


class Sutra4496:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.96: अग्निः'),
		('रामः', '', 'प.4.4.96: रामः'),
		('सीता', '', 'प.4.4.96: सीता'),
	]

