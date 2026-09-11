# Sutra प.4.2.89: शिखाया वलच्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — SiKAyA valac

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.89"
SUTRA_TEXT = "शिखाया वलच्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — SiKAyA valac"


class Sutra4289:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.89: अग्निः'),
		('रामः', '', 'प.4.2.89: रामः'),
		('सीता', '', 'प.4.2.89: सीता'),
	]

