# Sutra प.6.2.138: शितेर्नित्याबह्वज्बहुव्रीहावभसत्
# (Sandhi (euphonic combination)) — SiternityAbahvajbahuvrIhAvaBasat

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.138"
SUTRA_TEXT = "शितेर्नित्याबह्वज्बहुव्रीहावभसत्"
SUTRA_DESC = "(Sandhi (euphonic combination)) — SiternityAbahvajbahuvrIhAvaBasat"


class Sutra62138:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.138: अग्निः'),
		('रामः', '', 'प.6.2.138: रामः'),
		('सीता', '', 'प.6.2.138: सीता'),
	]

