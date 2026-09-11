# Sutra प.4.2.66: छन्दोब्राह्मणानि च तद्विषयाणि
# (Sup-sthāna (nominal endings) and kṛt-affixes) — CandobrAhmaRAni ca tadvizayARi

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.66"
SUTRA_TEXT = "छन्दोब्राह्मणानि च तद्विषयाणि"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — CandobrAhmaRAni ca tadvizayARi"


class Sutra4266:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.66: अग्निः'),
		('रामः', '', 'प.4.2.66: रामः'),
		('सीता', '', 'प.4.2.66: सीता'),
	]

