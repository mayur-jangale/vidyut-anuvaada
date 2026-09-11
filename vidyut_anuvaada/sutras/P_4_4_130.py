# Sutra प.4.4.130: ओजसोऽहनि यत्खौ
# (Sup-sthāna (nominal endings) and kṛt-affixes) — ojaso'hani yatKO

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.130"
SUTRA_TEXT = "ओजसोऽहनि यत्खौ"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — ojaso'hani yatKO"


class Sutra44130:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.130: अग्निः'),
		('रामः', '', 'प.4.4.130: रामः'),
		('सीता', '', 'प.4.4.130: सीता'),
	]

