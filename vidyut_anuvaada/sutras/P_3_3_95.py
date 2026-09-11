# Sutra प.3.3.95: स्थागापापचो भावे
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — sTAgApApaco BAve

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.95"
SUTRA_TEXT = "स्थागापापचो भावे"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — sTAgApApaco BAve"


class Sutra3395:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

