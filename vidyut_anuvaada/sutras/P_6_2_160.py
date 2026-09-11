# Sutra प.6.2.160: कृत्योकेष्णुच्चार्वादयश्च
# (Sandhi (euphonic combination)) — kftyokezRuccArvAdayaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.160"
SUTRA_TEXT = "कृत्योकेष्णुच्चार्वादयश्च"
SUTRA_DESC = "(Sandhi (euphonic combination)) — kftyokezRuccArvAdayaSca"


class Sutra62160:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.160: अग्निः'),
		('रामः', '', 'प.6.2.160: रामः'),
		('सीता', '', 'प.6.2.160: सीता'),
	]

