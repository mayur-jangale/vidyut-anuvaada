# Sutra प.6.1.98: अव्यक्तानुकरणस्यात इतौ
# sandhi-sūtra प.6.1.98

from P_6_1 import apply_6_1_98

SUTRA_CODE = "प.6.1.98"
SUTRA_TEXT = "अव्यक्तानुकरणस्यात इतौ"
SUTRA_DESC = "sandhi-sūtra प.6.1.98"


class Sutra6198:
	def apply(self, word, pos):
		return apply_6_1_98(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.98:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.98:marker=padartha;input=रामः'),
		('सीता', '', '6.1.98:marker=padartha;input=सीता'),
	]
