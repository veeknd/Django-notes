from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
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
        
        # if not self.request.user.is_anonymous:
        #     temp = User.objects.create_user(username="anon", email="none", first_name="none", last_name="none")
        #     temp.save()
        #     anonUser = User.objects.get(username='anon')
        #     self.request.user=User.objects.get(id=anonUser.id)
        qs = None
        if self.request.user.is_authenticated:
            qs = super(OwnerListView, self).get_queryset()
            qs = qs.filter(owner=self.request.user)
        return qs