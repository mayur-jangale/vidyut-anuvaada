# Sutra प.4.4.46: संज्ञायां ललाटकुक्कुट्यौ पश्यति
# (Sup-sthāna (nominal endings) and kṛt-affixes) — saMjYAyAM lalAwakukkuwyO paSyati

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.46"
SUTRA_TEXT = "संज्ञायां ललाटकुक्कुट्यौ पश्यति"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — saMjYAyAM lalAwakukkuwyO paSyati"


class Sutra4446:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.46: अग्निः'),
		('रामः', '', 'प.4.4.46: रामः'),
		('सीता', '', 'प.4.4.46: सीता'),
	]

