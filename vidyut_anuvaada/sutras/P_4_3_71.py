# Sutra प.4.3.71: छन्दसो यदणौ
# (Sup-sthāna (nominal endings) and kṛt-affixes) — Candaso yadaRO

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.71"
SUTRA_TEXT = "छन्दसो यदणौ"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — Candaso yadaRO"


class Sutra4371:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.71: अग्निः'),
		('रामः', '', 'प.4.3.71: रामः'),
		('सीता', '', 'प.4.3.71: सीता'),
	]

