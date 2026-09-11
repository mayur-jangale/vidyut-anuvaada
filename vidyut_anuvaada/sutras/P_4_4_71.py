# Sutra प.4.4.71: अध्यायिन्यदेशकालात्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — aDyAyinyadeSakAlAt

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.71"
SUTRA_TEXT = "अध्यायिन्यदेशकालात्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — aDyAyinyadeSakAlAt"


class Sutra4471:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.71: अग्निः'),
		('रामः', '', 'प.4.4.71: रामः'),
		('सीता', '', 'प.4.4.71: सीता'),
	]

