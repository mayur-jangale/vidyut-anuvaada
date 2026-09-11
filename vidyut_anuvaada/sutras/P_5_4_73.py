# Sutra प.5.4.73: बहुव्रीहौ संख्येये डजबहुगणात्
# (Strī-pratyaya and taddhita (feminine and secondary derivations)) — bahuvrIhO saMKyeye qajabahugaRAt

from sutra_engines import apply_general

SUTRA_CODE = "प.5.4.73"
SUTRA_TEXT = "बहुव्रीहौ संख्येये डजबहुगणात्"
SUTRA_DESC = "(Strī-pratyaya and taddhita (feminine and secondary derivations)) — bahuvrIhO saMKyeye qajabahugaRAt"


class Sutra5473:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.5.4.73: अग्निः'),
		('रामः', '', 'प.5.4.73: रामः'),
		('सीता', '', 'प.5.4.73: सीता'),
	]

