from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class OwnerCreateView (LoginRequiredMixin, CreateView):

    def form_valid(self,form):
        print("form valid called")
        object = form.save(commit=False)
        object.owner = self.request.user
        object.save()
        return super(OwnerCreateView,self).form_valid(form)

class OwnerListView(ListView):

    def get_queryset(self):
        print('update get_queryset called')
        """ Limit a User to only modifying their own data. """
        qs = super(OwnerListView, self).get_queryset()
        return qs.filter(owner=self.request.user)