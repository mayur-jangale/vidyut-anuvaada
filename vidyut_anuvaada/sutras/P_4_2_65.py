# Sutra प.4.2.65: सूत्राच्च कोपधात्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — sUtrAcca kopaDAt

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.65"
SUTRA_TEXT = "सूत्राच्च कोपधात्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — sUtrAcca kopaDAt"


class Sutra4265:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.65: अग्निः'),
		('रामः', '', 'प.4.2.65: रामः'),
		('सीता', '', 'प.4.2.65: सीता'),
	]

