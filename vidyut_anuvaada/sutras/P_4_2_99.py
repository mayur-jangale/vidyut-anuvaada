# Sutra प.4.2.99: कापिश्याः ष्फक्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kApiSyAH zPak

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.99"
SUTRA_TEXT = "कापिश्याः ष्फक्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kApiSyAH zPak"


class Sutra4299:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.99: अग्निः'),
		('रामः', '', 'प.4.2.99: रामः'),
		('सीता', '', 'प.4.2.99: सीता'),
	]

