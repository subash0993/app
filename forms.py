from django.forms import ModelForm
from .models import StudentsList


class StudentForm(ModelForm):
    class Meta:
        model = StudentsList
        fields = '__all__'
        # fields = ('studentId', 'firstName', 'lastName', 'markOne', 'markTwo', 'markThree', 'markFour',
        #           'markFive')


class FindStudent(ModelForm):
    class Meta:
        model = StudentsList
        fields = ('studentId',)


class DeleteStudent(ModelForm):
    class Meta:
        model = StudentsList
        fields = ('studentId',)
