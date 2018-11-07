import floppyforms as forms


class Slider(forms.RangeInput):
    min = 0
    step = 10
    max = 100
    template_name = 'slider.html'

    class Media:
        js = (
            'js/jquery.min.js',
            'js/jquery-ui.min.js',
        )
        css = {
            'all': (
                'css/jquery-ui.css',
            )
        }

class SlideForm(forms.Form):
    num = forms.IntegerField(widget=Slider)
    def clean_num(self):
        num = self.cleaned_data['num']
        if not 0 <= num <= 100:
            raise forms.ValidationError("Enter a value between 5 and 20")
        if not num % 10 == 0:
            raise forms.ValidationError("Enter a multiple of 5")
        return num
