# Sutra प.1.4.52: गतिबुद्धिप्रत्यवसानार्थशब्दकर्माकर्मकाणामणि कर्ता स णौ
# (Samjna (technical definitions)) — gatibudDipratyavasAnArTaSabdakarmAkarmakARAmaRi kartA sa RO

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.52"
SUTRA_TEXT = "गतिबुद्धिप्रत्यवसानार्थशब्दकर्माकर्मकाणामणि कर्ता स णौ"
SUTRA_DESC = "(Samjna (technical definitions)) — gatibudDipratyavasAnArTaSabdakarmAkarmakARAmaRi kartA sa RO"


class Sutra1452:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_52
		return apply_1_4_52(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-Ni-kartA:अग्निः'),
		('रामः', '', 'not-Ni-kartA:रामः'),
		('सीता', '', 'not-Ni-kartA:सीता'),
	]

