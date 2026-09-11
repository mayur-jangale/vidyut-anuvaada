# Sutra प.4.2.94: ग्रामाद्यखञौ
# (Sup-sthāna (nominal endings) and kṛt-affixes) — grAmAdyaKaYO

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.94"
SUTRA_TEXT = "ग्रामाद्यखञौ"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — grAmAdyaKaYO"


class Sutra4294:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.94: अग्निः'),
		('रामः', '', 'प.4.2.94: रामः'),
		('सीता', '', 'प.4.2.94: सीता'),
	]

