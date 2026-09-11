# Sutra प.5.2.79: शृङ्खलमस्य बन्धनं करभे
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — SfNKalamasya banDanaM karaBe

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.79"
SUTRA_TEXT = "शृङ्खलमस्य बन्धनं करभे"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — SfNKalamasya banDanaM karaBe"


class Sutra5279:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.79: अग्निः'),
		('रामः', '', 'प.5.2.79: रामः'),
		('सीता', '', 'प.5.2.79: सीता'),
	]

