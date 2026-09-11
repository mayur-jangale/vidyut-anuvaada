# Sutra प.1.1.2: अदेङ् गुणः
# Defines guṇa as the set of vowels {a, e, o}

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.2"
SUTRA_TEXT = "अदेङ् गुणः"
SUTRA_DESC = "Defines guṇa as the set of vowels {a, e, o}"


class Sutra112:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_2
		return apply_1_1_2(word, pos)

	EXAMPLES = [
		('नगः', '', 'guṇa={अ,ए,ओ};input=नगः;matches='),
		('एकः', '', 'guṇa={अ,ए,ओ};input=एकः;matches=ए'),
	]

