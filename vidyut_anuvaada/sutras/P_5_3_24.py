# Sutra प.5.3.24: इदमस्थमुः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — idamasTamuH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.24"
SUTRA_TEXT = "इदमस्थमुः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — idamasTamuH"


class Sutra5324:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.24: अग्निः'),
		('रामः', '', 'प.5.3.24: रामः'),
		('सीता', '', 'प.5.3.24: सीता'),
	]

