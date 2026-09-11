# Sutra प.7.3.25: जङ्गलधेनुवलजान्तस्य विभाषितमुत्तरम्
# (Taddhita (secondary derivations)) — jaNgalaDenuvalajAntasya viBAzitamuttaram

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.25"
SUTRA_TEXT = "जङ्गलधेनुवलजान्तस्य विभाषितमुत्तरम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — jaNgalaDenuvalajAntasya viBAzitamuttaram"


class Sutra7325:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.25: अग्निः'),
		('रामः', '', 'प.7.3.25: रामः'),
		('सीता', '', 'प.7.3.25: सीता'),
	]

