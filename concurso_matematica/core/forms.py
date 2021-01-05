from django import forms
from django.db.models.query import QuerySet

class CoreModelForm(forms.ModelForm):
    #name = forms.CharField(max_length=12, required=False)

    def __init__(self,  *args, **kwargs):

        #check function
        
        #Pop a queryset provided for filtering purposes through form field input
        queryset = kwargs.pop('queryset', None)
        super().__init__(*args, **kwargs)
        #self.checkfields()
        self.all_fields_not_required()

        if not queryset:
            self.queryset = self.__class__.Meta.model.objects.all()
           
        else:
            self.queryset = queryset

        self.filter()

    def filter(self):
        
        if self.is_valid():
            #if form is valid then program can proceed to filter  
            copy = self.cleaned_data.copy()
            for key in self.cleaned_data.keys():
                if not copy[key]:
                    copy.pop(key)
                else:
                    copy.setdefault(key+self.__class__.Meta.fields[key], copy.pop(key))
                
               # elif isinstance(self.cleaned_data[key], QuerySet):
               #     copy.setdefault(key+'__in', copy.pop(key))
                
            
            self.cleaned_data = copy

            print('filtered cleaned_data => ' + str(self.cleaned_data))
            self.qs = self.queryset.filter(**self.cleaned_data)
            

        else: 
            self.qs = self.queryset

        
    def all_fields_not_required(self):
        #This Function makes sure that all fields from any child of this class are not required.
        if hasattr(self.__class__.Meta, 'not_required'):
            if self.__class__.Meta.not_required == '__all__':
                for field in self.fields.values():
                    field.required = False
            else:
                for field_name in self.__class__.Meta.not_required:
                    self.fields[field_name].required = False


    
    def checkfields(self):
        #Check that the form fields are a subset of the model fields
        #Granting that every field defined here corresponds only to a model field 
        #and has its same name, no aditional input.

        list_ = []
        field_names = set(boundfield.name for boundfield in self)
        for model_field in self.__class__.Meta.model._meta.get_fields():
            list_.append(model_field.name)
        list_ = set(list_)
        print(list_, field_names)
        if field_names.issubset(list_):
            print('You are good to go')
        else:
            print('You have one or more fields whose name doesnt match with any of the corresponding model fields.')