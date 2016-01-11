import json
import sys

questions = json.load(sys.stdin)

def convert(v1):
	incorrect_answers = [{'answer': answer} for answer in v1['bogus']]
	correct_answer = {'answer': v1['answer'], 'correct': 'true'}

	return {
		'answers': incorrect_answers + [correct_answer],
		'question': v1['line'],
		'explanation': v1['explanation'],
		'id': v1['id']
	}

print json.dumps([convert(question) for question in questions])
