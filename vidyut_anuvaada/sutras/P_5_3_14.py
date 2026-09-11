# Sutra प.5.3.14: इतराभ्योऽपि दृश्यन्ते
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — itarAByo'pi dfSyante

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.14"
SUTRA_TEXT = "इतराभ्योऽपि दृश्यन्ते"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — itarAByo'pi dfSyante"


class Sutra5314:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.14: अग्निः'),
		('रामः', '', 'प.5.3.14: रामः'),
		('सीता', '', 'प.5.3.14: सीता'),
	]

