# Sutra प.6.2.170: जातिकालसुखादिभ्योऽनाच्छादनात् क्तोऽकृतमितप्रतिपन्नाः
# (Sandhi (euphonic combination)) — jAtikAlasuKAdiByo'nAcCAdanAt kto'kftamitapratipannAH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.170"
SUTRA_TEXT = "जातिकालसुखादिभ्योऽनाच्छादनात् क्तोऽकृतमितप्रतिपन्नाः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — jAtikAlasuKAdiByo'nAcCAdanAt kto'kftamitapratipannAH"


class Sutra62170:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.170: अग्निः'),
		('रामः', '', 'प.6.2.170: रामः'),
		('सीता', '', 'प.6.2.170: सीता'),
	]

