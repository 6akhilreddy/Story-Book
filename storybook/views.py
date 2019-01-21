from django.shortcuts import render,redirect
from .models import Story
from .forms import WriteForm

def index(request):

	content=Story.objects.order_by('-date_added')

	context={'content' : content}

	return render(request, 'storybook/index.html', context)

def readstory(request,read_id):

	visits=request.session.get('visits',0)
	request.session['visits']=visits+1


	content=Story.objects.get(pk=read_id)
	context={'content':content,
	'visits':visits}
	return render(request, 'storybook/readstory.html', context )

def addstory(request):

	if request.method == 'POST':
		form=WriteForm(request.POST)

		if form.is_valid():
			new_story=Story(title=form.cleaned_data['title'],
				brief=form.cleaned_data['brief'],
				description=form.cleaned_data['description'])
			new_story.save()
			return redirect('index')
	else:
		form=WriteForm()

	context={'form':form}
	return render(request, 'storybook/addstory.html', context)


