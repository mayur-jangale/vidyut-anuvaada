# Sutra प.4.2.116: काश्यादिभ्यष्ठञ्ञिठौ
# (Sup-sthāna (nominal endings) and kṛt-affixes) — kASyAdiByazWaYYiWO

from sutra_engines import apply_general

SUTRA_CODE = "प.4.2.116"
SUTRA_TEXT = "काश्यादिभ्यष्ठञ्ञिठौ"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — kASyAdiByazWaYYiWO"


class Sutra42116:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.2.116: अग्निः'),
		('रामः', '', 'प.4.2.116: रामः'),
		('सीता', '', 'प.4.2.116: सीता'),
	]

