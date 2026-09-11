# Sutra प.4.2.5: संज्ञायां श्रवणाश्वत्थाभ्याम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — saMjYAyAM SravaRASvatTAByAm

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.5"
SUTRA_TEXT = "संज्ञायां श्रवणाश्वत्थाभ्याम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — saMjYAyAM SravaRASvatTAByAm"


class Sutra425:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.5: अग्निः'),
		('रामः', '', 'प.4.2.5: रामः'),
		('सीता', '', 'प.4.2.5: सीता'),
	]

