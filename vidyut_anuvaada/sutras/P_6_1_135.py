# Sutra प.6.1.135: सुट् कात् पूर्वः
# sandhi-sūtra प.6.1.135

from P_6_1 import apply_6_1_135

SUTRA_CODE = "प.6.1.135"
SUTRA_TEXT = "सुट् कात् पूर्वः"
SUTRA_DESC = "sandhi-sūtra प.6.1.135"


class Sutra61135:
	def apply(self, word, pos):
		return apply_6_1_135(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.135:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.135:marker=padartha;input=रामः'),
		('सीता', '', '6.1.135:marker=padartha;input=सीता'),
	]
