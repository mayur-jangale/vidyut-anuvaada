# Sutra प.4.3.15: श्वसस्तुट् च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — Svasastuw ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.15"
SUTRA_TEXT = "श्वसस्तुट् च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — Svasastuw ca"


class Sutra4315:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.15: अग्निः'),
		('रामः', '', 'प.4.3.15: रामः'),
		('सीता', '', 'प.4.3.15: सीता'),
	]

