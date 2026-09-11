# Sutra प29: karmaRi dfSividoH sAkalye
# karmaRi dfSividoH sAkalye

from sutra_engines import apply_general
from P_3_4 import apply_3_4_29

SUTRA_CODE = "प29"
SUTRA_TEXT = "karmaRi dfSividoH sAkalye"
SUTRA_DESC = "karmaRi dfSividoH sAkalye"


class Sutra3429:
	def apply(self, word, pos):
		return apply_3_4_29(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-029:karmaRi dfSividoH sAkalye;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-029:karmaRi dfSividoH sAkalye;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-029:karmaRi dfSividoH sAkalye;input=सीता;stem=सीता;ending=-;pos='),
	]

