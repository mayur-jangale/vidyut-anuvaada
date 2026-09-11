# Sutra प.5.2.86: पूर्वादिनिः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — pUrvAdiniH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.86"
SUTRA_TEXT = "पूर्वादिनिः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — pUrvAdiniH"


class Sutra5286:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.86: अग्निः'),
		('रामः', '', 'प.5.2.86: रामः'),
		('सीता', '', 'प.5.2.86: सीता'),
	]

