from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import TeamMember, Update, Risk, Deliverable
from django.forms import ModelForm


"""Must include this override since TeamMembers are extended admin users"""
class TeamMemberCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = TeamMember
        fields = ('username', 'email')

"""Must include this override since TeamMembers are extended admin users"""
class TeamMemberChangeForm(UserChangeForm):

    class Meta:
        model = TeamMember
        fields = ('username', 'email')


""" Update Form class. Each field is made read-only to prevent editing except
    the multichoice fields as seems difficult to enforce this """
class UpdateForm(ModelForm):
    # queryset = TeamMember.objects.all()
    log = forms.CharField(widget=forms.Textarea(attrs={'readonly':'readonly'}))
    date = forms.DateField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'readonly':'readonly'}))
    # author = forms.models.ModelChoiceField(widget=forms.Select(queryset))
    #deliverable = forms.ChoiceField(widget=forms.RadioSelect(attrs={'disabled': 'disabled'}))

    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['author'].widget.attrs['readonly'] = True

    class Meta:
        model = Update
        exclude =[]



""" Defines the form for Deliverable that is seen in Django Admin"""
class DeliverableForm(ModelForm):

    class Meta:
        model = Deliverable
        exclude = []

    
    def __init__(self, *args, **kwargs):
        super(DeliverableForm, self).__init__(*args, **kwargs)

        # This is how we set initial form fields in django admin
        self.initial["status_message"] = ""


        # Here are 4 ways NOT to set the initial value of a form field:
        """
        self.fields["status_message"].initial = ""
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            # 1
            instance.status_message = forms.CharField(widget=forms.Textarea(), initial="")
            # 2
            instance.status_message = ""
        # 3
        if self.is_valid():
            form.cleaned_data["status_message"] = ""
        """

    # 4 (included because we want to set the widget)
    status_message = forms.CharField(max_length = 200, widget=forms.Textarea(), initial="")
    

    