from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

class ObjectDetailMixin:

    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})


class ObjectCreateMixin:

    form = None
    template = None

    def get(self, request):
        form = self.form
        return render(request, self.template, context={'form': form})


    def post(self, request):
        bound_form = self.form(request.POST)
        if bound_form.is_valid():
            obj = bound_form.save()
            return redirect(obj)
        return render(request, self.template, context={'form': bound_form})


class ObjectEditMixin:
    model = None
    form = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.form(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.form(request.POST, instance=obj)
        if bound_form.is_valid():
            bound_form.save()
            return redirect(obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})


class ObjectDeleteMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect("index_url")      


class Englishficator:
    letters = {
        'а': 'a', 
        'б': 'b', 
        'в': 'v', 
        'г': 'g', 
        'д': 'd', 
        'е': 'e', 
        'ё': 'yo', 
        'ж': 'j', 
        'з': 'z', 
        'и': 'i', 
        'й': 'y', 
        'к': 'k', 
        'л': 'l', 
        'м': 'm', 
        'н': 'n', 
        'о': 'o', 
        'п': 'p', 
        'р': 'r', 
        'с': 's', 
        'т': 't', 
        'у': 'u', 
        'ф': 'f', 
        'х': 'h', 
        'ц': 'c', 
        'ч': 'ch', 
        'ш': 'sh', 
        'щ': 'sch', 
        'ь': '\'', 
        'ы': 'i', 
        'ъ': '', 
        'э': 'e', 
        'ю': 'yu', 
        'я': 'ya'}


    def __call__(self, string):
        transformed_string = ''
        for letter in string:
            if letter.lower() in self.letters.keys():
                letter = self.letters[letter.lower()]
            transformed_string += (letter)
        return transformed_string