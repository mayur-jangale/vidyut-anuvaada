# Sutra प.4.2.104: अव्ययात्त्यप्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — avyayAttyap

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.104"
SUTRA_TEXT = "अव्ययात्त्यप्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — avyayAttyap"


class Sutra42104:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.104: अग्निः'),
		('रामः', '', 'प.4.2.104: रामः'),
		('सीता', '', 'प.4.2.104: सीता'),
	]

