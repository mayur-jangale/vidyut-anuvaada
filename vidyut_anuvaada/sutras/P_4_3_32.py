# Sutra प.4.3.32: सिन्ध्वपकराभ्यां कन्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — sinDvapakarAByAM kan

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.32"
SUTRA_TEXT = "सिन्ध्वपकराभ्यां कन्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — sinDvapakarAByAM kan"


class Sutra4332:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.32: अग्निः'),
		('रामः', '', 'प.4.3.32: रामः'),
		('सीता', '', 'प.4.3.32: सीता'),
	]

