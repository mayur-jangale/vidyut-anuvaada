# Sutra प.6.1.192: भीह्रीभृहुमदजनधनदरिद्राजागरां प्रत्ययात् पूर्वम् पिति
# sandhi-sūtra प.6.1.192

from P_6_1 import apply_6_1_192

SUTRA_CODE = "प.6.1.192"
SUTRA_TEXT = "भीह्रीभृहुमदजनधनदरिद्राजागरां प्रत्ययात् पूर्वम् पिति"
SUTRA_DESC = "sandhi-sūtra प.6.1.192"


class Sutra61192:
	def apply(self, word, pos):
		return apply_6_1_192(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.192:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.192:marker=padartha;input=रामः'),
		('सीता', '', '6.1.192:marker=padartha;input=सीता'),
	]
