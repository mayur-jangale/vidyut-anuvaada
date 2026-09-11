# Sutra प.4.2.142: कन्थापलदनगरग्रामहृदोत्तरपदात्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kanTApaladanagaragrAmahfdottarapadAt

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.142"
SUTRA_TEXT = "कन्थापलदनगरग्रामहृदोत्तरपदात्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kanTApaladanagaragrAmahfdottarapadAt"


class Sutra42142:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.142: अग्निः'),
		('रामः', '', 'प.4.2.142: रामः'),
		('सीता', '', 'प.4.2.142: सीता'),
	]

