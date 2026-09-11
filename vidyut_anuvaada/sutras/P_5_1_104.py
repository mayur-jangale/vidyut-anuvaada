# Sutra प.5.1.104: समयस्तदस्य प्राप्तम्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — samayastadasya prAptam

from sutra_engines import apply_general

SUTRA_CODE = "प.5.1.104"
SUTRA_TEXT = "समयस्तदस्य प्राप्तम्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — samayastadasya prAptam"


class Sutra51104:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.1.104: अग्निः'),
		('रामः', '', 'प.5.1.104: रामः'),
		('सीता', '', 'प.5.1.104: सीता'),
	]

