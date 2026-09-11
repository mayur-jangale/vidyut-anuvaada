# Sutra प.6.2.168: नाव्ययदिक्शब्दगोमहत्स्थूलमुष्टिपृथुवत्सेभ्यः
# (Sandhi (euphonic combination)) — nAvyayadikSabdagomahatsTUlamuzwipfTuvatseByaH

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.168"
SUTRA_TEXT = "नाव्ययदिक्शब्दगोमहत्स्थूलमुष्टिपृथुवत्सेभ्यः"
SUTRA_DESC = "(Sandhi (euphonic combination)) — nAvyayadikSabdagomahatsTUlamuzwipfTuvatseByaH"


class Sutra62168:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.168: अग्निः'),
		('रामः', '', 'प.6.2.168: रामः'),
		('सीता', '', 'प.6.2.168: सीता'),
	]

