# Sutra प.3.3.137: कालविभागे चानहोरात्राणाम्
# (Vikarana and tiṅ-pratyaya (verbal affix operations)) — kAlaviBAge cAnahorAtrARAm

from sutra_engines import apply_general

SUTRA_CODE = "प.3.3.137"
SUTRA_TEXT = "कालविभागे चानहोरात्राणाम्"
SUTRA_DESC = "(Vikarana and tiṅ-pratyaya (verbal affix operations)) — kAlaviBAge cAnahorAtrARAm"


class Sutra33137:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'vikaraṇa: अग्निः'),
		('रामः', '', 'vikaraṇa: रामः'),
		('सीता', '', 'vikaraṇa: सीता'),
	]

