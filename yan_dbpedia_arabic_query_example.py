from yan_dbpedia_arabic_query import *

'''

http://localhost:4522/app/discover#/view/b8e759c0-81c6-11ec-8ba5-492ad581a6be

http://localhost:4522/app/dashboards#/view/2b844c60-8012-11ec-b7d6-bb167b339ae4

http://localhost:4522/app/dashboards#/view/c2d53e60-7fa1-11ec-a4ee-9134f5c69475

'''

##########


text = u"""
أنا من دبي
"""

entities = text_entity_linking(text)

for e in entities:
	print(e)


'''
{'document_id': '3d2bbb392ba408b1694433417e7b8beb', 'entity': '67cb773dc48f6880e485731893d5deb1', 'entity_dbpedia_id': '<http://ar.dbpedia.org/resource/إل_(مغني)>', 'entity_name': 'إل (مغني)', 'entity_name_main': 'إل ', 'entity_type': 'Actor', 'entity_word': 'إل', 'entity_word_hash': '4cf118e93ccab6031103557ef6d7789a', 'entity_word_popularity': 202, 'entity_word_rank': 1, 'entity_name_comment': 'مغني'}
{'document_id': '7134f3800ef955d2e5f884db6aca3ff5', 'entity': '79cb41bfa531b1af6e531f20c4436d7e', 'entity_dbpedia_id': '<http://ar.dbpedia.org/resource/مغني>', 'entity_name': 'مغني', 'entity_name_main': 'مغني', 'entity_type': 'occupation', 'entity_word': 'مغني', 'entity_word_hash': 'ca2dc141435e8ed7d65d2b5168000225', 'entity_word_popularity': 6, 'entity_word_rank': 1}
'''


###

text = u"""
انا من ابوظبي
"""

entities = text_entity_linking(text)

for e in entities:
	print(e)


'''
{'document_id': 'dba56a4830b771dfc1d1744a3b97f565', 'entity': '7702b3333b72107676d32b7c6ac4a0fc', 'entity_dbpedia_id': '<http://ar.dbpedia.org/resource/أبو_ظبي>', 'entity_name': 'أبو ظبي', 'entity_name_main': 'أبو ظبي', 'entity_type': 'locationCity', 'entity_word': 'ظبي', 'entity_word_hash': '735dd48f8e137071f02f8907c88ee368', 'entity_word_popularity': 8, 'entity_word_rank': 1}
{'document_id': '2609957379d1c75404d3237ece8b8091', 'entity': '8ca353fbf1a88b37d7afe33acf88952d', 'entity_dbpedia_id': '<http://ar.dbpedia.org/resource/هي_(مان!)>', 'entity_name': 'هي (مان!)', 'entity_name_main': 'هي ', 'entity_type': 'Album', 'entity_word': 'هي', 'entity_word_hash': '487dd24054f499af233dc6d9594ec4d2', 'entity_word_popularity': 66, 'entity_word_rank': 1, 'entity_name_comment': 'مان!'}
{'document_id': '8ba8b980059f24c9fc97460a3e1566d7', 'entity': '3866651c5246600502045d2778d53b7d', 'entity_dbpedia_id': '<http://ar.dbpedia.org/resource/دولة_الإمارات_العربية_المتحدة>', 'entity_name': 'دولة الإمارات العربية المتحدة', 'entity_name_main': 'دولة الإمارات العربية المتحدة', 'entity_type': 'deathPlace', 'entity_word': 'دولة', 'entity_word_hash': '029a4d819c598ccac41b619c97497206', 'entity_word_popularity': 10, 'entity_word_rank': 1}
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