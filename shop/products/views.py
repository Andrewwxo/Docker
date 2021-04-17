from django.shortcuts import render
from .models import Product
from .tasks import save_products
from django.views.generic import ListView, TemplateView, DetailView, FormView
from .forms import MessageForm


class ProductListView(ListView):
    model = Product
    template_name = 'products/index.html'


class AboutTemplateView(TemplateView):
    template_name = 'products/about.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'


class MessageFormView(FormView):
    form_class = MessageForm
    template_name = 'products/message.html'
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


def index_view(request):

    # products = Product.objects.all()
    products = Product.objects.select_related('kind', 'kind__product')
    context = {
        'products': products,
        'shop_name': 'Доставка продуктов'
    }

    # if request.method == "POST":
    #     save_products.delay()

    return render(request, 'products/index.html', context=context)
