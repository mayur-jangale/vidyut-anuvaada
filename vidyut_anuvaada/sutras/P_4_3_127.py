# Sutra प.4.3.127: संघाङ्कलक्षणेष्वञ्यञिञामण्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — saMGANkalakzaRezvaYyaYiYAmaR

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.127"
SUTRA_TEXT = "संघाङ्कलक्षणेष्वञ्यञिञामण्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — saMGANkalakzaRezvaYyaYiYAmaR"


class Sutra43127:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.127: अग्निः'),
		('रामः', '', 'प.4.3.127: रामः'),
		('सीता', '', 'प.4.3.127: सीता'),
	]

