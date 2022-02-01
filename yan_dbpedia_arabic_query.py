############yan_dbpedia_arabic_query.py##############
import re 
import hashlib
import jessica_es


md5_str = lambda input: hashlib.md5(input.encode()).hexdigest()

es_session = jessica_es.start_es(
	es_path = "/yan/elasticsearch_dbpedia_arabic",
	es_port_number = "5987")

'''
localhost:5987/entity/_search?pretty=true
'''


'''

text = u"""
إل هو مغني جيد
"""

entities = text_entity_linking(text)

for e in entities:
	print('\n')
	print(e)

###

text = u"""
أعيش في أبو ظبي وأعمل في دبي
"""

entities = text_entity_linking(text)

for e in entities:
	print('\n')
	print(e)


'''

def text_entity_linking(
	text,
	):
	output = []
	'''
	prepare the text for matching
	'''
	text = re.sub(r'\s+', r'  ', text.strip())
	text = ' '+text.strip()+' '
	'''
	split text to words
	'''
	words = text.strip().split(r'  ')
	words = list(set(words))
	'''
	search the words in the word index
	'''
	candidate_entities = []
	for w in words:
		#print(w)
		search_results = jessica_es.search_doc_by_filter(
			index_name = 'entity_word',
			field_name = 'entity_word_hash',
			entity_name = md5_str(w),
			es_session = es_session,
			return_entity_max_number = 10000)
		candidate_entities += search_results
		#print(search_results)
	'''
	parepare the candidate entities for matching and return matched results
	'''
	candidate_entities =  [dict(t) for t in {tuple(d.items()) for d in candidate_entities}]
	candidate_entities1 = {}
	for e in candidate_entities:
		entity_key = re.sub(r'\s+', r'  ', e['entity_name_main'].strip())
		candidate_entities1[entity_key] = e
	'''
	make a regex rule from the candidate entity names
	'''
	entity_names = [re.escape(k) for k in candidate_entities1]
	entity_names = sorted(entity_names, key=len, reverse=True)
	re_candidate_words = '(^| )(?P<entity>('+'|'.join(entity_names)+'))($| )'
	'''
	detect entity from text
	'''
	matched_entity_names = []
	for m in re.finditer(
		re_candidate_words,
		text,
		):
		matched_entity_names.append(m.group('entity'))
	'''
	return the matched entities
	'''
	for k in matched_entity_names:
		'''
		if the entity main name is too short, and the comment is not null
		also need to match the comment
		'''
		if len(k) <= 3 and 'entity_name_comment' in candidate_entities1[k]:
			#print(candidate_entities1[k])
			comment = re.sub(r'\s+', r'  ', candidate_entities1[k]['entity_name_comment'].strip())
			comment = " "+comment+" "
			comment = re.escape(comment)
			comment_in = bool(re.search(comment, text))
			if comment_in:
				output.append(candidate_entities1[k])
		else:
			output.append(candidate_entities1[k])		
	return output


'''

entity_name = u"جدة"

find_entity_by_name(
	entity_name,
	)

'''
def find_entity_by_name(
	entity_name,
	):
	try:
		result = jessica_es.search_doc_by_match(
			index_name = 'entity',
			field_name = "entity_name",
			entity_name = entity_name,
			es_session = es_session,
			return_entity_max_number = 1,
			return_entity_min_score = 5.0)
		return result[0]['entity']
	except:
		return None



'''
entity_name = u"أبو ظبي	"

find_entity_by_main_name(
	entity_name,
	)

'''
def find_entity_by_main_name(
	entity_name,
	):
	try:
		result = jessica_es.search_doc_by_match(
			index_name = 'entity',
			field_name = "entity_name_main",
			entity_name = entity_name,
			es_session = es_session,
			return_entity_max_number = 1,
			return_entity_min_score = 5.0)
		return result[0]['entity']
	except:
		return None


'''

http://localhost:4522/app/dashboards#/view/c2d53e60-7fa1-11ec-a4ee-9134f5c69475

query_entities = [
	'e9905107bdcb017f617f4c4a9b3c3da2',
	]

triplets = find_triplets_of_entities(
	query_entities = query_entities,
	)

for t in triplets:
	print(t)

'''

def find_triplets_of_entities(
	query_entities,
	):
	triplets = []
	for entity in query_entities:
		try:
			triplets += jessica_es.search_doc_by_filter(
				index_name = 'relation',
				field_name = 'subject',
				entity_name = entity,
				es_session = es_session,
				return_entity_max_number = 10000)
		except:
			pass
		try:
			triplets += jessica_es.search_doc_by_filter(
				index_name = 'relation',
				field_name = 'object',
				entity_name = entity,
				es_session = es_session,
				return_entity_max_number = 10000)
		except:
			pass
	triplets = [dict(t) for t in {tuple(d.items()) for d in triplets}]
	return triplets



'''
find_top_subject_object_for_each_entity(
	entities = query_entities,
	triplets = triplets,
	top_triplet_number = 5,
	)
'''

def find_top_subject_object_for_each_entity(
	entities,
	triplets,
	top_triplet_number = 5,
	):
	output = []
	for e in entities:
		try:
			##
			e_as_subject = list(filter(lambda t: t['subject'] == e, triplets))
			e_as_subject.sort(key=lambda t: t['object_out_degree'], reverse = True)
			e_as_subject = e_as_subject[0:top_triplet_number]
			output += e_as_subject
		except:
			pass
		try:
			##
			e_as_object = list(filter(lambda t: t['object'] == e, triplets))
			e_as_object.sort(key=lambda t: t['subject_out_degree'], reverse = True)
			e_as_object = e_as_object[0:top_triplet_number]
			output += e_as_object
		except:
			pass
	##
	output = [dict(t) for t in {tuple(d.items()) for d in output}]
	return output


'''
find_top_relations_between_entity_pairs(
	entities = query_entities,
	triplets = triplets,
	top_triplet_number = 3,
	)
'''

def find_top_relations_between_entity_pairs(
	entities,
	triplets,
	top_triplet_number = 3,
	):
	output = []
	for subject in entities:
		for object in entities:
			if subject != object:
				try:
					relation_triplet = list(filter(lambda t: 
						t['subject'] == subject 
						and t['object'] == object, triplets))
					output += relation_triplet
				except:
					pass
	output = [dict(t) for t in {tuple(d.items()) for d in output}]
	return output



'''
find_top_common_subject_object_of_entity_pairs(
	entities = query_entities,
	triplets = triplets,
	top_triplet_number = 3,
	)
'''

def find_top_common_subject_object_of_entity_pairs(
	entities,
	triplets,
	top_triplet_number = 3,
	):
	output = []
	for e1 in entities:
		for e2 in entities:
			if e1 < e2:
				###########
				e1_as_subject = list(filter(lambda t: 
					t['subject'] == e1, triplets))
				e1_object = [
					{'object':t['object'],
					'object_out_degree':t['object_out_degree'],
					} for t in e1_as_subject]
				##
				e2_as_subject = list(filter(lambda t: 
					t['subject'] == e2, triplets))
				e2_object = [
					{'object':t['object'],
					'object_out_degree':t['object_out_degree'],
					} for t in e2_as_subject]
				##
				e1_e2_common_object = [x for x in e1_object if x in e2_object]
				e1_e2_common_object.sort(key=lambda t: t['object_out_degree'], reverse = True)
				e1_e2_common_object = e1_e2_common_object[0:top_triplet_number]
				e1_e2_common_object = [t['object'] for t in e1_e2_common_object]
				###
				e1_as_subject = list(filter(lambda t: 
					t['object'] in e1_e2_common_object, e1_as_subject))
				e2_as_subject = list(filter(lambda t: 
					t['object'] in e1_e2_common_object, e2_as_subject))
				###
				output += e1_as_subject
				output += e2_as_subject
				###########
				e1_as_object = list(filter(lambda t: 
					t['object'] == e1, triplets))
				e1_subject = [
					{'subject':t['subject'],
					'subject_out_degree':t['subject_out_degree'],
					} for t in e1_as_object]
				##
				e2_as_object = list(filter(lambda t: 
					t['object'] == e2, triplets))
				e2_subject = [
					{'subject':t['subject'],
					'subject_out_degree':t['subject_out_degree'],
					} for t in e2_as_object]
				##
				e1_e2_common_subject = [x for x in e1_subject if x in e2_subject]
				e1_e2_common_subject.sort(key=lambda t: t['subject_out_degree'], reverse = True)
				e1_e2_common_subject = e1_e2_common_subject[0:top_triplet_number]
				e1_e2_common_subject = [t['subject'] for t in e1_e2_common_subject]
				###
				e1_as_object = list(filter(lambda t: 
					t['subject'] in e1_e2_common_subject, e1_as_object))
				e2_as_object = list(filter(lambda t: 
					t['subject'] in e1_e2_common_subject, e2_as_object))
				###
				output += e1_as_object
				output += e2_as_object
	output = [dict(t) for t in {tuple(d.items()) for d in output}]
	return output

############yan_dbpedia_arabic_query.py##############