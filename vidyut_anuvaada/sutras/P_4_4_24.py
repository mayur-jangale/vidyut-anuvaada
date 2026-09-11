# Sutra प.4.4.24: लवणाल्लुक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — lavaRAlluk

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.24"
SUTRA_TEXT = "लवणाल्लुक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — lavaRAlluk"


class Sutra4424:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.24: अग्निः'),
		('रामः', '', 'प.4.4.24: रामः'),
		('सीता', '', 'प.4.4.24: सीता'),
	]

