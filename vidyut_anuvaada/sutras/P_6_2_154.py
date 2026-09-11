# Sutra प.6.2.154: मिश्रं चानुपसर्गमसंधौ
# (Sandhi (euphonic combination)) — miSraM cAnupasargamasaMDO

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.154"
SUTRA_TEXT = "मिश्रं चानुपसर्गमसंधौ"
SUTRA_DESC = "(Sandhi (euphonic combination)) — miSraM cAnupasargamasaMDO"


class Sutra62154:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.154: अग्निः'),
		('रामः', '', 'प.6.2.154: रामः'),
		('सीता', '', 'प.6.2.154: सीता'),
	]

