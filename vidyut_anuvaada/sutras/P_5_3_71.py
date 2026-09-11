# Sutra प.5.3.71: अव्ययसर्वनाम्नामकच् प्राक् टेः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — avyayasarvanAmnAmakac prAk weH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.3.71"
SUTRA_TEXT = "अव्ययसर्वनाम्नामकच् प्राक् टेः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — avyayasarvanAmnAmakac prAk weH"


class Sutra5371:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.3.71: अग्निः'),
		('रामः', '', 'प.5.3.71: रामः'),
		('सीता', '', 'प.5.3.71: सीता'),
	]

