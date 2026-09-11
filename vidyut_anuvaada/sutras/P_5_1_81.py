# Sutra प.5.1.81: मासाद्वयसि यत्खञौ
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — mAsAdvayasi yatKaYO

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.81"
SUTRA_TEXT = "मासाद्वयसि यत्खञौ"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — mAsAdvayasi yatKaYO"


class Sutra5181:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.81: अग्निः'),
		('रामः', '', 'प.5.1.81: रामः'),
		('सीता', '', 'प.5.1.81: सीता'),
	]

