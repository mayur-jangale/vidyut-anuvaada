# Sutra प.1.4.62: अनुकरणं चानितिपरम्
# (Samjna (technical definitions)) — anukaraRaM cAnitiparam

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.62"
SUTRA_TEXT = "अनुकरणं चानितिपरम्"
SUTRA_DESC = "(Samjna (technical definitions)) — anukaraRaM cAnitiparam"


class Sutra1462:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_62
		return apply_1_4_62(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-anukaraNa:अग्निः'),
		('रामः', '', 'not-anukaraNa:रामः'),
		('सीता', '', 'not-anukaraNa:सीता'),
	]

