# Sutra प.4.3.7: ग्रामजनपदैकदेशादञ्ठञौ
# (Sup-sthāna (nominal endings) and kṛt-affixes) — grAmajanapadEkadeSAdaYWaYO

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.7"
SUTRA_TEXT = "ग्रामजनपदैकदेशादञ्ठञौ"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — grAmajanapadEkadeSAdaYWaYO"


class Sutra437:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.7: अग्निः'),
		('रामः', '', 'प.4.3.7: रामः'),
		('सीता', '', 'प.4.3.7: सीता'),
	]

