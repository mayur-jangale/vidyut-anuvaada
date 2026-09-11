# Sutra प.5.4.97: उपमानादप्राणिषु
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — upamAnAdaprARizu

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.97"
SUTRA_TEXT = "उपमानादप्राणिषु"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — upamAnAdaprARizu"


class Sutra5497:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.97: अग्निः'),
		('रामः', '', 'प.5.4.97: रामः'),
		('सीता', '', 'प.5.4.97: सीता'),
	]

