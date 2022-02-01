# dbpedia_query_arabic

## pull the docker


```
docker pull yanliang12/yan_dbpedia_arabic_query:1.0.2
```

### start the docker

```
docker run -it ^
-p 5987:5987 ^
-p 4522:4522 ^
yanliang12/yan_dbpedia_arabic_query:1.0.2 ^
python3
```

### test the example

```python
>>> from yan_dbpedia_arabic_query import *
>>>
>>> text = u"""
... إل هو مغني جيد
... """
>>>
>>> entities = text_entity_linking(text)
>>>
>>> for e in entities:
...     print(e)
...
{'document_id': '3d2bbb392ba408b1694433417e7b8beb', 'entity': '67cb773dc48f6880e485731893d5deb1', 'entity_dbpedia_id': '<http://ar.dbpedia.org/resource/إل_(مغني)>', 'entity_name': 'إل (مغني)', 'entity_name_main': 'إل ', 'entity_type': 'Actor', 'entity_word': 'إل', 'entity_word_hash': '4cf118e93ccab6031103557ef6d7789a', 'entity_word_popularity': 202, 'entity_word_rank': 1, 'entity_name_comment': 'مغني'}
{'document_id': '7134f3800ef955d2e5f884db6aca3ff5', 'entity': '79cb41bfa531b1af6e531f20c4436d7e', 'entity_dbpedia_id': '<http://ar.dbpedia.org/resource/مغني>', 'entity_name': 'مغني', 'entity_name_main': 'مغني', 'entity_type': 'occupation', 'entity_word': 'مغني', 'entity_word_hash': 'ca2dc141435e8ed7d65d2b5168000225', 'entity_word_popularity': 6, 'entity_word_rank': 1}
>>>
>>> text = u"""
... أعيش في أبو ظبي وأعمل في دبي
... """
>>>
>>> entities = text_entity_linking(text)
>>>
>>> for e in entities:
...     print(e)
...
{'document_id': 'dba56a4830b771dfc1d1744a3b97f565', 'entity': '7702b3333b72107676d32b7c6ac4a0fc', 'entity_dbpedia_id': '<http://ar.dbpedia.org/resource/أبو_ظبي>', 'entity_name': 'أبو ظبي', 'entity_name_main': 'أبو ظبي', 'entity_type': 'locationCity', 'entity_word': 'ظبي', 'entity_word_hash': '735dd48f8e137071f02f8907c88ee368', 'entity_word_popularity': 8, 'entity_word_rank': 1}
{'document_id': 'c85b16ab874f4481381b2ecf5ab92fc1', 'entity': '9a57177fcc2b6f203998a28a878488c7', 'entity_dbpedia_id': '<http://ar.dbpedia.org/resource/دبي>', 'entity_name': 'دبي', 'entity_name_main': 'دبي', 'entity_type': 'residence', 'entity_word': 'دبي', 'entity_word_hash': '30f6afc588cc90e827ec7673a2b450b5', 'entity_word_popularity': 32, 'entity_word_rank': 1}
>>>
>>>
>>> ##########
>>>
>>> find_entity_by_name(
...     entity_name = u"جدة",
...     )
'bfb5f138aa0def5a85636296a41a52ec'
>>>
>>>
>>> find_entity_by_main_name(
...     entity_name = u"أبو ظبي",
...     )
'7702b3333b72107676d32b7c6ac4a0fc'
>>>
>>> ##########
>>>
>>> query_entities = [
...     'e9905107bdcb017f617f4c4a9b3c3da2',
...     ]
>>>
>>> triplets = find_triplets_of_entities(
...     query_entities = query_entities,
...     )
>>>
>>> find_top_subject_object_for_each_entity(
...     entities = query_entities,
...     triplets = triplets,
...     top_triplet_number = 5,
...     )
[{'document_id': 'f128d72a641740db7c8fc4d88089537a', 'subject_dbpedia_id': '<http://ar.dbpedia.org/resource/دومزداي:_يوم_القيامة_(فيلم)>', 'object_dbpedia_id': '<http://ar.dbpedia.org/resource/تيلر_بتس>', 'subject': 'e9905107bdcb017f617f4c4a9b3c3da2', 'object': '7254670a07137d422d1fb12edd8c4687', 'relation': 'musicComposer', 'subject_name': 'دومزداي: يوم القيامة (فيلم)', 'object_name': 'تيلر بتس', 'subject_type': 'Film', 'object_type': 'musicComposer', 'subject_out_degree': 38, 'object_out_degree': 0}, {'document_id': '85fce5a40e75cd909715f4923e111089', 'subject_dbpedia_id': '<http://ar.dbpedia.org/resource/دومزداي:_يوم_القيامة_(فيلم)>', 'object_dbpedia_id': '<http://ar.dbpedia.org/resource/سام_مكوردي>', 'subject': 'e9905107bdcb017f617f4c4a9b3c3da2', 'object': 'a0fdb93fc1933c33f68fce7cf663dc86', 'relation': 'cinematography', 'subject_name': 'دومزداي: يوم القيامة (فيلم)', 'object_name': 'سام مكوردي', 'subject_type': 'Film', 'object_type': 'cinematography', 'subject_out_degree': 38, 'object_out_degree': 0}, {'document_id': '3b3aa702751977aaca053960e47855fa', 'subject_dbpedia_id': '<http://ar.dbpedia.org/resource/دومزداي:_يوم_القيامة_(فيلم)>', 'object_dbpedia_id': '<http://ar.dbpedia.org/resource/يونيفرسال_بيكتشرز>', 'subject': 'e9905107bdcb017f617f4c4a9b3c3da2', 'object': '79b23d724129bd74888e9ff078775607', 'relation': 'distributor', 'subject_name': 'دومزداي: يوم القيامة (فيلم)', 'object_name': 'يونيفرسال بيكتشرز', 'subject_type': 'Film', 'object_type': 'distributor', 'subject_out_degree': 38, 'object_out_degree': 1}, {'document_id': 'f8b7eb4bafa0093bf4e4f56b5526e6c6', 'subject_dbpedia_id': '<http://ar.dbpedia.org/resource/دومزداي:_يوم_القيامة_(فيلم)>', 'object_dbpedia_id': '<http://ar.dbpedia.org/resource/المملكة_المتحدة>', 'subject': 'e9905107bdcb017f617f4c4a9b3c3da2', 'object': '0817c969e0d3d82fbc6439d304057352', 'relation': 'country', 'subject_name': 'دومزداي: يوم القيامة (فيلم)', 'object_name': 'المملكة المتحدة', 'subject_type': 'Film', 'object_type': 'country', 'subject_out_degree': 38, 'object_out_degree': 781}, {'document_id': 'ab5465ad887469507c288fa277134953', 'subject': 'e9905107bdcb017f617f4c4a9b3c3da2', 'object': '8dd74cdb97b510b9af8ee651377ccf71', 'relation': 'starring', 'subject_name': 'دومزداي: يوم القيامة (فيلم)', 'object_name': 'رونا ميترا', 'subject_type': 'Film', 'object_type': 'Actor', 'subject_out_degree': 38, 'object_out_degree': 47}]
>>>
>>>
>>> ##########
>>>
>>> query_entities = [
...     '069900d767e9eeb2a571bcdaf72ca499',
...     'e59a1d228892b5d22759611e9a2c88b2',
...     ]
>>>
>>> triplets = find_triplets_of_entities(
...     query_entities = query_entities,
...     )
>>>
>>> find_top_relations_between_entity_pairs(
...     entities = query_entities,
...     triplets = triplets,
...     top_triplet_number = 3,
...     )
[{'document_id': 'fff81a19fcc5446bc93f86d4d3f74f2b', 'subject_dbpedia_id': '<http://ar.dbpedia.org/resource/أحمد_بن_راشد_آل_مكتوم>', 'object_dbpedia_id': '<http://ar.dbpedia.org/resource/بر_دبي>', 'subject': '069900d767e9eeb2a571bcdaf72ca499', 'object': 'e59a1d228892b5d22759611e9a2c88b2', 'relation': 'birthPlace', 'subject_name': 'أحمد بن راشد آل مكتوم', 'object_name': 'بر دبي', 'subject_type': 'Person', 'object_type': 'birthPlace', 'subject_out_degree': 23, 'object_out_degree': 24}]
>>>
>>> ##########
>>>
>>> query_entities = [
...     '2e067ec09b93ffb37714c5005cc09e23',
...     'ababe0cbff53fb45517b04e0747ecf57',
...     ]
>>>
>>> triplets = find_triplets_of_entities(
...     query_entities = query_entities,
...     )
>>>
>>> find_top_common_subject_object_of_entity_pairs(
...     entities = query_entities,
...     triplets = triplets,
...     top_triplet_number = 3,
...     )
[{'document_id': '82266ecff38b048ca2dcb428e63502ed', 'subject_dbpedia_id': '<http://ar.dbpedia.org/resource/عارف_الشيخ_عبد_الله_الحسن>', 'object_dbpedia_id': '<http://ar.dbpedia.org/resource/دبي>', 'subject': 'ababe0cbff53fb45517b04e0747ecf57', 'object': '9a57177fcc2b6f203998a28a878488c7', 'relation': 'birthPlace', 'subject_name': 'عارف الشيخ عبد الله الحسن', 'object_name': 'دبي', 'subject_type': 'Writer', 'object_type': 'birthPlace', 'subject_out_degree': 51, 'object_out_degree': 238}, {'document_id': 'dc428ba00473c4f19c47b54bef5c9df4', 'subject_dbpedia_id': '<http://ar.dbpedia.org/resource/نجوم_الغانم>', 'object_dbpedia_id': '<http://ar.dbpedia.org/resource/دبي>', 'subject': '2e067ec09b93ffb37714c5005cc09e23', 'object': '9a57177fcc2b6f203998a28a878488c7', 'relation': 'birthPlace', 'subject_name': 'نجوم الغانم', 'object_name': 'دبي', 'subject_type': 'Person', 'object_type': 'birthPlace', 'subject_out_degree': 22, 'object_out_degree': 238}]
>>>
>>> ##########
```
