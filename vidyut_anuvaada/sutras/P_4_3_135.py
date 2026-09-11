# Sutra प.4.3.135: अवयवे च प्राण्योषधिवृक्षेभ्यः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — avayave ca prARyozaDivfkzeByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.135"
SUTRA_TEXT = "अवयवे च प्राण्योषधिवृक्षेभ्यः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — avayave ca prARyozaDivfkzeByaH"


class Sutra43135:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.135: अग्निः'),
		('रामः', '', 'प.4.3.135: रामः'),
		('सीता', '', 'प.4.3.135: सीता'),
	]

