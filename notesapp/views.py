from django.shortcuts import render
from django.http import  HttpResponse, HttpResponseRedirect
from notesapp.forms import UserForm, UserProfileForm, NoteForm, LabelForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import  User
from notesapp.models import UserProfile, Note, Label
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    if 'user_id' in request.session:
        user_obj=User.objects.filter(id=request.session['user_id'])
        note_obj=Note.objects.filter(user_id=request.session['user_id'])
        data=RequestContext(request, {'user_id':request.session['user_id'],
                                      'user':user_obj, 'note':note_obj, 'a':0})
        return render_to_response('notesapp/index.html', data)
    else:
        return render_to_response('notesapp/index.html', {})

def all_notes(request):
    if 'user_id' in request.session:
        note_obj=Note.objects.filter(permit='Y').exclude(user_id=request.session['user_id'])
        return render(request, 'notesapp/all_notes.html', {'notes':note_obj})

def register(request):
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()

            return HttpResponseRedirect("/notes/")

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
        'notesapp/register.html',
        {'user_form': user_form, 'profile_form': profile_form } )

def auth_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        error="Invalid login details!"
        inactive="The user is inactive! "
        dict_err={"error":error}
        dict_inactive={'error':inactive}
        if user:
            if user.is_active:
                login(request, user)
                request.session['user_id'] = user.id
                return HttpResponseRedirect('/notes/')
            else:
                return render(request, 'notesapp/login.html', dict_inactive)
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return render(request, 'notesapp/login.html', dict_err)

    else:
        return render(request, 'notesapp/login.html', {})

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/notes/')

def add_note(request):
    if request.method=='POST':

        note_form=NoteForm(data=request.POST)

        if note_form.is_valid():
            # note_obj=Note(note_name=request.POST.get('note_name'),
            #           note_body=request.POST.get('note_body'),
            #               user_id=request.session['user_id'])
            note_form.instance.user = request.user
            #note_form.user = request.session['user_id']
            #note_form.user_id=request.session['user_id']
            note_form.save()
            # note_obj.save()
            #note_obj.labels.add(labels=request.POST.get('labels'))
            return HttpResponseRedirect('/notes/')
    else:
        note_form = NoteForm()


    return render(request,
        'notesapp/add_note.html',
        {'note_form': note_form, 'user_id':request.session['user_id'] } )

def edit_note(request, note_id):
    #note_obj=Note.objects.filter(id=note_id)
    #if request.GET:
    if request.method=='GET':
        note_obj=Note.objects.get(id=note_id)
        note_form = NoteForm(instance=note_obj)
        #note_obj=Note.objects,filter(id=request.POST.get('id')).update(note_obj=request.POST.get('note_body'))
        return render(request, 'notesapp/edit_note.html', {'note': note_form})
    #elif request.method == 'POST':
    else:
        note_obj=Note.objects.filter(id=note_id)
        note_obj.update(note_name=request.POST.get('note_name'))
        note_obj.update(note_body=request.POST.get('note_body'))
        note_obj.update(color=request.POST.get('color'))
        #note_obj=Note.objects.filter(id=note_id)
        note_obj[0].labels=[]
        #note_obj.update(labels=request.POST.get('labels'))

        for label in request.POST.getlist('labels'):
            print(label)
            note_obj[0].labels.add(Label.objects.get(id=label))
        #note_form = NoteForm(data=request.POST)
        #if note_form.is_valid():
         #   note_obj=Note(note_name=request.POST.get('note_name'),
         #             note_body=request.POST.get('note_body'), user_id=request.session['user_id'])
         #   note_obj.save()
        return HttpResponseRedirect('/notes/')

def delete_note(request, note_id):
    Note.objects.get(id=note_id).delete()
    return HttpResponseRedirect('/notes/')

@login_required()
def see_note(request, note_id):
    note_obj=Note.objects.get(id=note_id)
    if   note_obj.user== request.user or note_obj.permit=='Y':
        return render(request, 'notesapp/see_note.html', {'note':note_obj})
    else:
        return HttpResponseRedirect('/notes/')

def add_label(request):
    if request.method=='POST':
        label_form=LabelForm(data=request.POST)
        if label_form.is_valid():
            label_form.save()
            return HttpResponseRedirect("/notes/add_note/")
    else:
        label_form = LabelForm()

    return render(request,
        'notesapp/add_label.html',
        {'label_form': label_form } )



