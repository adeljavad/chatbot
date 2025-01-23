from django import forms

class SQLQueryForm(forms.Form):
    query = forms.CharField(
        widget=forms.Textarea(attrs={'id': 'sql-editor', 'rows': 10, 'cols': 80}),
        label='SQL Query'
    )