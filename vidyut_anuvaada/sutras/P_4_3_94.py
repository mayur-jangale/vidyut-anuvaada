# Sutra प.4.3.94: तूदीशलातुरवर्मतीकूचवाराड्ढक्छण्ढञ्यकः
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tUdISalAturavarmatIkUcavArAqQakCaRQaYyakaH

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.94"
SUTRA_TEXT = "तूदीशलातुरवर्मतीकूचवाराड्ढक्छण्ढञ्यकः"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tUdISalAturavarmatIkUcavArAqQakCaRQaYyakaH"


class Sutra4394:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.94: अग्निः'),
		('रामः', '', 'प.4.3.94: रामः'),
		('सीता', '', 'प.4.3.94: सीता'),
	]

