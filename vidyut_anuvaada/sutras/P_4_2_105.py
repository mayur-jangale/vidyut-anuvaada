# Sutra प.4.2.105: ऐषमोह्यःश्वसोऽन्यतरस्याम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — EzamohyaHSvaso'nyatarasyAm

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.105"
SUTRA_TEXT = "ऐषमोह्यःश्वसोऽन्यतरस्याम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — EzamohyaHSvaso'nyatarasyAm"


class Sutra42105:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.105: अग्निः'),
		('रामः', '', 'प.4.2.105: रामः'),
		('सीता', '', 'प.4.2.105: सीता'),
	]

