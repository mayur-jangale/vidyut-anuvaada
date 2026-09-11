# Sutra प.5.3.49: प्रागेकादशभ्योऽच्छन्दसि
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — prAgekAdaSaByo'cCandasi

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.49"
SUTRA_TEXT = "प्रागेकादशभ्योऽच्छन्दसि"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — prAgekAdaSaByo'cCandasi"


class Sutra5349:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.49: अग्निः'),
		('रामः', '', 'प.5.3.49: रामः'),
		('सीता', '', 'प.5.3.49: सीता'),
	]

