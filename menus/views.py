from django.views.generic import CreateView, UpdateView, DetailView, ListView

from .models import Item
from .forms import ItemForm


class ItemListView(ListView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemDetailView(DetailView):
    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemCreateView(CreateView):
    form_class = ItemForm
    template_name = 'form.html'
    success_url = '/items/'
    login_url = '/login/'  # overrides global login url in the settings

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(ItemCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ItemCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Menu Item'
        return context


class ItemUpdateView(UpdateView):
    form_class = ItemForm

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

