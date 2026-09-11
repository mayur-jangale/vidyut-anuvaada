# Sutra प.5.2.36: तदस्य संजातं तारकादिभ्य इतच्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadasya saMjAtaM tArakAdiBya itac

from sutra_engines import apply_general

SUTRA_CODE = "प.5.2.36"
SUTRA_TEXT = "तदस्य संजातं तारकादिभ्य इतच्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — tadasya saMjAtaM tArakAdiBya itac"


class Sutra5236:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.2.36: अग्निः'),
		('रामः', '', 'प.5.2.36: रामः'),
		('सीता', '', 'प.5.2.36: सीता'),
	]

