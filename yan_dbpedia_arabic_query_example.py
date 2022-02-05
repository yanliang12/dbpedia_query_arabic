from yan_dbpedia_arabic_query import *

'''

http://localhost:4522/app/discover#/view/b8e759c0-81c6-11ec-8ba5-492ad581a6be

http://localhost:4522/app/dashboards#/view/2b844c60-8012-11ec-b7d6-bb167b339ae4

http://localhost:4522/app/dashboards#/view/c2d53e60-7fa1-11ec-a4ee-9134f5c69475

'''

##########

text = u"""
أعمل في الدوحة ولكني أعيش في أبو ظبي
"""

entities = text_entity_linking(text)

for e in entities:
	print(e)


'''
{'document_id': 'd70e2d49c43a68701641135559e018f1', 'entity': '7a36ab8c99c32695edc3c984c6f9e0a1', 'entity_dbpedia_id': '<http://ar.dbpedia.org/resource/الدوحة>', 'entity_name': 'الدوحة', 'entity_name_main': 'الدوحة', 'entity_type': 'Settlement', 'entity_word': 'الدوحة', 'entity_word_hash': '868fe5876ece69f59962f961b7581934', 'entity_word_popularity': 5, 'entity_word_rank': 1, 'entity_out_degree': 104.0, 'matching_method': 'entity_out_degree'}
{'document_id': 'dba56a4830b771dfc1d1744a3b97f565', 'entity': '7702b3333b72107676d32b7c6ac4a0fc', 'entity_dbpedia_id': '<http://ar.dbpedia.org/resource/أبو_ظبي>', 'entity_name': 'أبو ظبي', 'entity_name_main': 'أبو ظبي', 'entity_type': 'locationCity', 'entity_out_degree': 2.0, 'entity_word': 'ظبي', 'entity_word_hash': '735dd48f8e137071f02f8907c88ee368', 'entity_word_popularity': 8, 'entity_word_rank': 1, 'matching_method': 'entity_name_long'}
'''

##########

find_entity_by_name(
	entity_name = u"دبي",
	)

#'9a57177fcc2b6f203998a28a878488c7'

find_entity_by_main_name(
	entity_name = u"أبو ظبي	",
	)

#'7702b3333b72107676d32b7c6ac4a0fc'

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