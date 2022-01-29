from yan_dbpedia_arabic_query import *

##########

find_entity_by_name(
	entity_name = u"جدة",
	)


find_entity_by_main_name(
	entity_name = u"أبو ظبي	",
	)

##########

query_entities = [
	'e9905107bdcb017f617f4c4a9b3c3da2',
	]

triplets = find_triplets_of_entities(
	query_entities = query_entities,
	)

find_top_subject_object_for_each_entity(
	entities = query_entities,
	triplets = triplets,
	top_triplet_number = 5,
	)


##########

query_entities = [
	'069900d767e9eeb2a571bcdaf72ca499',
	'e59a1d228892b5d22759611e9a2c88b2',
	]

triplets = find_triplets_of_entities(
	query_entities = query_entities,
	)

find_top_relations_between_entity_pairs(
	entities = query_entities,
	triplets = triplets,
	top_triplet_number = 3,
	)

##########

query_entities = [
	'2e067ec09b93ffb37714c5005cc09e23',
	'ababe0cbff53fb45517b04e0747ecf57',
	]

triplets = find_triplets_of_entities(
	query_entities = query_entities,
	)

find_top_common_subject_object_of_entity_pairs(
	entities = query_entities,
	triplets = triplets,
	top_triplet_number = 3,
	)

##########