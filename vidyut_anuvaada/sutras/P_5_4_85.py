# Sutra प.5.4.85: उपसर्गादध्वनः
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — upasargAdaDvanaH

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.85"
SUTRA_TEXT = "उपसर्गादध्वनः"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — upasargAdaDvanaH"


class Sutra5485:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.85: अग्निः'),
		('रामः', '', 'प.5.4.85: रामः'),
		('सीता', '', 'प.5.4.85: सीता'),
	]

