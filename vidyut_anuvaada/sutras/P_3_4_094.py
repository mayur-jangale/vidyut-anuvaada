# Sutra प94: leTo aDAwO
# leTo aDAwO liG-ASiSi

from sutra_engines import apply_general
from P_3_4 import apply_3_4_94

SUTRA_CODE = "प94"
SUTRA_TEXT = "leTo aDAwO"
SUTRA_DESC = "leTo aDAwO liG-ASiSi"


class Sutra3494:
	def apply(self, word, pos):
		return apply_3_4_94(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-094:leTo aDAwO liG-ASiSi;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-094:leTo aDAwO liG-ASiSi;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-094:leTo aDAwO liG-ASiSi;input=सीता;stem=सीता;ending=-;pos='),
	]

