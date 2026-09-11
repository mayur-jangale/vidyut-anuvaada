# Sutra प.4.4.131: वेशोयशआदेर्भगाद्यल्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — veSoyaSaAderBagAdyal

from sutra_engines import apply_general

SUTRA_CODE = "प.4.4.131"
SUTRA_TEXT = "वेशोयशआदेर्भगाद्यल्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — veSoyaSaAderBagAdyal"


class Sutra44131:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.4.131: अग्निः'),
		('रामः', '', 'प.4.4.131: रामः'),
		('सीता', '', 'प.4.4.131: सीता'),
	]

