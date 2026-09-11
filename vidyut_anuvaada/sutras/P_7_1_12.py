# Sutra प.7.1.12: टाङसिङसामिनात्स्याः
# (Taddhita (secondary derivations)) — wANasiNasAminAtsyAH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.12"
SUTRA_TEXT = "टाङसिङसामिनात्स्याः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — wANasiNasAminAtsyAH"


class Sutra7112:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.12: अग्निः'),
		('रामः', '', 'प.7.1.12: रामः'),
		('सीता', '', 'प.7.1.12: सीता'),
	]

