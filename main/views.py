from django.shortcuts import render
from .forms import GetNumber


def homepage(request):
    name = 'Kirill Pastuhov'
    task = 'Prime factorization of a given number'
    return render(request=request, template_name="main/home.html", context={"name": name, "task": task})


#  Handling GET and POST requests
#  For POST request validate the form and return prime factorization of a given number.


def test_task(request):
    result = []
    if request.method == 'POST':
        form = GetNumber(request.POST)
        if form.is_valid():
            n = (form.cleaned_data.get("your_number"))
            result = primfacs(n)
            return render(request, "main/test_task.html", context={"form": form, "result": result, "value": n})
    form = GetNumber()
    return render(request, "main/test_task.html", context={"form": form})


#  Function for computing prime factorization of a  given number


def primfacs(n):
    i = 2
    primfac = [1]
    while i * i <= n:
        while n % i == 0:
            primfac.append(int(i))
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(int(n))

    return primfac
