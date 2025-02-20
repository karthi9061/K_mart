from django import template

register=template.Library()

@register.filter(name='row_split')
def multiply(list_data,row_size):
    r_sp=[]
    i=0
    for data in list_data:
        r_sp.append(data)
        i=i+1
        if i==row_size:
            i=0
            yield r_sp
            r_sp=[]
    yield r_sp        