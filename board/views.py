from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Sale, Bid
from .forms import SaleForm, BidForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets
from .serializers import SaleSerializer, BidSerializer
from django_filters.rest_framework import DjangoFilterBackend

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['id']


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['buyer_id', 'agreed']


def index(request):
    page = request.GET.get('page', '1')
    sale_list = Sale.objects.order_by('-create_date')
    paginator = Paginator(sale_list, 10)
    page_obj = paginator.get_page(page)
    context = {'sale_list': page_obj}
    return render(request, 'board/sale_list.html', context)


def detail(request, sale_id):
    sale = get_object_or_404(Sale, pk=sale_id)
    context = {'sale': sale}
    return render(request, 'board/sale_detail.html', context)


@login_required(login_url='common:login')
def bid_create(request, sale_id):
    sale = get_object_or_404(Sale, pk=sale_id)
    if request.method == "POST":
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.buyer = request.user
            bid.create_date = timezone.now()
            bid.sale = sale
            bid.save()
            return redirect('board:detail', sale_id=sale.id)
    else:
        form = BidForm()
    context = {'sale': sale, 'form': form}
    return render(request, 'board/sale_detail.html', context)


@login_required(login_url='common:login')
def sale_create(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.seller = request.user
            sale.create_date = timezone.now()
            sale.save()
            return redirect('board:index')
    else:
        form = SaleForm()
    context = {'form': form}
    return render(request, 'board/sale_form.html', context)


@login_required(login_url='common:login')
def sale_modify(request, sale_id):
    sale = get_object_or_404(Sale, pk=sale_id)
    if request.user != sale.seller:
        messages.error(request, 'You have no right to Modify')
        return redirect('board:detail', sale_id=sale.id)
    if request.method == "POST":
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.modify_date = timezone.now()
            sale.save()
            return redirect('board:detail', sale_id=sale.id)
    else:
        form = SaleForm(instance=sale)
    context = {'form': form}
    return render(request, 'board/sale_form.html', context)


@login_required(login_url='common:login')
def sale_delete(request, sale_id):
    sale = get_object_or_404(Sale, pk=sale_id)
    if request.user != sale.seller:
        messages.error(request, 'You have no right to delete it.')
        return redirect('board:detail', sale_id=sale.id)
    sale.delete()
    return redirect('board:index')


@login_required(login_url='common:login')
def bid_accept(request, bid_id):
    bid = get_object_or_404(Bid, pk=bid_id)
    if request.user != bid.sale.seller:
        messages.error(request, 'Only Seller can accept the trade request')
        return redirect('board:detail', sale_id=bid.sale.id)
    if not bid.agreed and not bid.sale.sold:
        bid.agreed = True
        bid.sale.sold = True
        bid.save()
        bid.sale.save()
        return redirect('board:detail', sale_id=bid.sale.id)
    else:
        messages.error(request, 'You already accepted the trade request')
        return redirect('board:detail', sale_id=bid.sale.id)