# Sutra प76: kto aDikaraRe ca
# kto'DikaraRe ca DROvya

from sutra_engines import apply_general
from P_3_4 import apply_3_4_76

SUTRA_CODE = "प76"
SUTRA_TEXT = "kto aDikaraRe ca"
SUTRA_DESC = "kto'DikaraRe ca DROvya"


class Sutra3476:
	def apply(self, word, pos):
		return apply_3_4_76(word, pos)

	EXAMPLES = [
	('अग्निः', '', "p34-076:kto'DikaraRe ca DROvya;input=अग्निः;stem=अग्निः;ending=-;pos="),
		('रामः', '', "p34-076:kto'DikaraRe ca DROvya;input=रामः;stem=रामः;ending=-;pos="),
		('सीता', '', "p34-076:kto'DikaraRe ca DROvya;input=सीता;stem=सीता;ending=-;pos="),
	]

