# Sutra प.7.3.90: ऊर्णोतेर्विभाषा
# (Taddhita (secondary derivations)) — UrRoterviBAzA

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.90"
SUTRA_TEXT = "ऊर्णोतेर्विभाषा"
SUTRA_DESC = "(Taddhita (secondary derivations)) — UrRoterviBAzA"


class Sutra7390:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.90: अग्निः'),
		('रामः', '', 'प.7.3.90: रामः'),
		('सीता', '', 'प.7.3.90: सीता'),
	]

