# Sutra प.4.2.115: भवतष्ठक्छसौ
# (Sup-sthāna (nominal endings) and kṛt-affixes) — BavatazWakCasO

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.115"
SUTRA_TEXT = "भवतष्ठक्छसौ"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — BavatazWakCasO"


class Sutra42115:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.115: अग्निः'),
		('रामः', '', 'प.4.2.115: रामः'),
		('सीता', '', 'प.4.2.115: सीता'),
	]

