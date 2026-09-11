# Sutra प.1.1.23: बहुगणवतुडति संख्या
# (Samjna (technical definitions)) — bahugaRavatuqati saMKyA

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.23"
SUTRA_TEXT = "बहुगणवतुडति संख्या"
SUTRA_DESC = "(Samjna (technical definitions)) — bahugaRavatuqati saMKyA"


class Sutra1123:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_23
		return apply_1_1_23(word, pos)

	EXAMPLES = [
		('त्रि', '', 'संख्या:त्रि;known=yes'),
		('दश', '', 'संख्या:दश;known=yes'),
		('नव', '', 'संख्या:नव;known=yes'),
		('ईश्वर', '', 'संख्या:ईश्वर;known=no'),
	]

