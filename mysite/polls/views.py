from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[1:5]
	context = 
	return render(request, 'index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'details.html'{'question': question})

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'results.html', {'question': question})


def vote(request, question_id):
	# respone = 'You chosed for %s'
	# return HttpResponse(response % question_id)
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'details.html',
			{'question': question, 'error_message': 'Ne vybral otvet'})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))