# Sutra प.4.3.93: सिन्धुतक्षशिलादिभ्योऽणञौ
# (Sup-sthāna (nominal endings) and kṛt-affixes) — sinDutakzaSilAdiByo'RaYO

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.93"
SUTRA_TEXT = "सिन्धुतक्षशिलादिभ्योऽणञौ"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — sinDutakzaSilAdiByo'RaYO"


class Sutra4393:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.93: अग्निः'),
		('रामः', '', 'प.4.3.93: रामः'),
		('सीता', '', 'प.4.3.93: सीता'),
	]

