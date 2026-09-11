# Sutra प.3.2.124: लटः शतृशानचावप्रथमासमानाधिकरणे
# bhrauṅ — specific PPP formation

from sutra_engines import apply_general

SUTRA_CODE = "प.3.2.124"
SUTRA_TEXT = "लटः शतृशानचावप्रथमासमानाधिकरणे"
SUTRA_DESC = "bhrauṅ — specific PPP formation"


class Sutra32124:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

