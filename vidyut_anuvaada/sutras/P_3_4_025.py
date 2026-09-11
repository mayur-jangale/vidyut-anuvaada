# Sutra प25: karmaRyAkroSe kfYaH khamuY
# karmaRi AkroSe kfYaH khamuY

from sutra_engines import apply_general
from P_3_4 import apply_3_4_25

SUTRA_CODE = "प25"
SUTRA_TEXT = "karmaRyAkroSe kfYaH khamuY"
SUTRA_DESC = "karmaRi AkroSe kfYaH khamuY"


class Sutra3425:
	def apply(self, word, pos):
		return apply_3_4_25(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-025:karmaRi AkroSe kfYaH khamuY;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-025:karmaRi AkroSe kfYaH khamuY;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-025:karmaRi AkroSe kfYaH khamuY;input=सीता;stem=सीता;ending=-;pos='),
	]

