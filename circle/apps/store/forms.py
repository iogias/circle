from django import forms


class UserInfoForm(forms.Form):
    pass
    # def create_form(self, code):
    #     if code == 'mobile_legends':
    #         first_param = forms.CharField(label="User Id", max_length=64, required=True)
    #         second_param = forms.CharField(label="Zone Id", max_length=64)
    #         return first_param, second_param
