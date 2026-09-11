# Sutra प.4.3.10: द्वीपादनुसमुद्रं यञ्
# (Sup-sthāna (nominal endings) and kṛt-affixes) — dvIpAdanusamudraM yaY

from sutra_engines import apply_general

SUTRA_CODE = "प.4.3.10"
SUTRA_TEXT = "द्वीपादनुसमुद्रं यञ्"
SUTRA_DESC = "(Sup-sthāna (nominal endings) and kṛt-affixes) — dvIpAdanusamudraM yaY"


class Sutra4310:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.4.3.10: अग्निः'),
		('रामः', '', 'प.4.3.10: रामः'),
		('सीता', '', 'प.4.3.10: सीता'),
	]

