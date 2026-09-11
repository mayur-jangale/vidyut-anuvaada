# Sutra प.4.2.35: महाराजप्रोष्ठपदाट्ठञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — mahArAjaprozWapadAwWaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.35"
SUTRA_TEXT = "महाराजप्रोष्ठपदाट्ठञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — mahArAjaprozWapadAwWaY"


class Sutra4235:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.35: अग्निः'),
		('रामः', '', 'प.4.2.35: रामः'),
		('सीता', '', 'प.4.2.35: सीता'),
	]

