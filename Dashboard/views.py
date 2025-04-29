from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Order.models import OrderModel
from Products.models import ProductsModel
from django.db.models import Sum
from Item.models import ItemModel
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from calendar import month_name
# Create your views here.
@login_required(login_url = '/customadmin/login')
def loaddashboard(request):
    order = OrderModel.objects.all()
    product = ProductsModel.objects.all()
    allproduct = ProductsModel.objects.all()
    allusers = User.objects.all()
    allorders = OrderModel.objects.all()
    total_payment_sum = OrderModel.objects.aggregate(Sum('total_payment'))
    total_payment_sum_value = total_payment_sum['total_payment__sum']
    top_5_selling_products = (ItemModel.objects
                          .values('product_id')  # Group by product_id
                          .annotate(total_qty_sold=Sum('qty'))  # Sum the quantity sold for each product
                          .order_by('-total_qty_sold')  # Order by the quantity sold in descending order
                          [:5])  # Get top 5 products

    # Step 2: Use the product_id values from the query to fetch product details
    product_ids = [item['product_id'] for item in top_5_selling_products]

    # Step 3: Retrieve the related products (ProductModel) and match with the result
    products = ProductsModel.objects.filter(product_id__in=product_ids)
    topsellingdata = []
    for item in top_5_selling_products:
        product =  products.get(product_id=item['product_id'])
        topsellingdata.append({"title":product.title,"img1":product.img1,"sell_price":product.sell_price,"sell":item['total_qty_sold']})

    monthly_sales = (
        OrderModel.objects
        .annotate(month=TruncMonth('orderdatetime'))
        .values('month')
        .annotate(total_sales=Sum('total_payment'))
        .order_by('month')
    )

    # Format the result with month names
    sales_data = [
        {"month": month_name[entry['month'].month], "total_sales": entry['total_sales']}
        for entry in monthly_sales
    ]
    
    
    context={
        "orderdata":order,
        "productdata":product,
        "allproduct":len(allproduct),
        "allusers":len(allusers),
        "allorders":len(allorders),
        "total_payment_sum_value":total_payment_sum_value,
        "top_5_selling_products":topsellingdata,
        "sales_data":sales_data
    }
    return render(request,'admin/dashboard.html',context)