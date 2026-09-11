# Sutra प.7.1.23: स्वमोर्नपुंसकात्
# (Taddhita (secondary derivations)) — svamornapuMsakAt

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.23"
SUTRA_TEXT = "स्वमोर्नपुंसकात्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — svamornapuMsakAt"


class Sutra7123:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.23: अग्निः'),
		('रामः', '', 'प.7.1.23: रामः'),
		('सीता', '', 'प.7.1.23: सीता'),
	]

