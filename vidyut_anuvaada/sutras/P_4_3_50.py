# Sutra प.4.3.50: संवत्सराग्रहायणीभ्यां ठञ् च
# (Sup-sthāna (nominal endings) and kṛt-affixes) — saMvatsarAgrahAyaRIByAM WaY ca

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.50"
SUTRA_TEXT = "संवत्सराग्रहायणीभ्यां ठञ् च"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — saMvatsarAgrahAyaRIByAM WaY ca"


class Sutra4350:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.50: अग्निः'),
		('रामः', '', 'प.4.3.50: रामः'),
		('सीता', '', 'प.4.3.50: सीता'),
	]

