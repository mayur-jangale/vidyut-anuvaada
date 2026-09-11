# Sutra प.4.2.109: उदीच्यग्रामाच्च बह्वचोऽन्तोदात्तात्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — udIcyagrAmAcca bahvaco'ntodAttAt

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.109"
SUTRA_TEXT = "उदीच्यग्रामाच्च बह्वचोऽन्तोदात्तात्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — udIcyagrAmAcca bahvaco'ntodAttAt"


class Sutra42109:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.109: अग्निः'),
		('रामः', '', 'प.4.2.109: रामः'),
		('सीता', '', 'प.4.2.109: सीता'),
	]

