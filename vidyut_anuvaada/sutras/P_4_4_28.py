# Sutra प.4.4.28: तत् प्रत्यनुपूर्वमीपलोमकूलम्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — tat pratyanupUrvamIpalomakUlam

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.28"
SUTRA_TEXT = "तत् प्रत्यनुपूर्वमीपलोमकूलम्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — tat pratyanupUrvamIpalomakUlam"


class Sutra4428:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.28: अग्निः'),
		('रामः', '', 'प.4.4.28: रामः'),
		('सीता', '', 'प.4.4.28: सीता'),
	]

