from django.shortcuts import render


def home(request):
	query = request.GET.get('name')
	message = "Some {} simple text".format(query)
	template = "home.html"
	context = {
			'message' : message,

	}
	return render(request, template, context)