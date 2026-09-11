# Sutra प.4.2.2: लाक्षारोचनाशकलकर्दमाट्ठक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — lAkzArocanASakalakardamAwWak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.2"
SUTRA_TEXT = "लाक्षारोचनाशकलकर्दमाट्ठक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — lAkzArocanASakalakardamAwWak"


class Sutra422:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.2: अग्निः'),
		('रामः', '', 'प.4.2.2: रामः'),
		('सीता', '', 'प.4.2.2: सीता'),
	]

