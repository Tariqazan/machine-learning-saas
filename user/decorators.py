from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


class BasicSubscription(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.service == 'Basic':
            return True
        else:
            return redirect('login') 


class StandardSubscription(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.service == 'Standard':
            return True
        else:
            return redirect('login') 


class PremiumSubscription(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.service == 'Premium':
            return True
        else:
            return redirect('login') 