from django.urls import path, include
from rest_framework.routers import DefaultRouter

# views
from core.apps.address.views import AddressView, CountryView, StateView
from core.apps.cart.views import CartView, CouponView, WishlistView, PointsView
from core.apps.content.views import BlogView, FaqView, NotificationView, QuestionsView, ImageView
from core.apps.core.views import TransactionView, WalletsView
from core.apps.orders.views import OrderstatusView, OrderView, RefundView
from core.apps.payments.views import CurrencyView, PaymentaccountView
from core.apps.product.views import (
    AttributeView,
    AttributevalueView,
    CompareitemView,
    CompareView,
    CategoryView,
    ProductView,
    ReviewView,
    StoreView,
    TagsView,
    VariationView
)


router = DefaultRouter()

# address views
router.register(r'address', AddressView, basename='address')
router.register(r'country', CountryView, basename='country')
router.register(r'state', StateView, basename='state')

# cart views
router.register(r'cart', CartView, basename='cart')
router.register(r'wishlist', WishlistView, basename='wishlist')
router.register(r'coupon', CouponView, basename='coupon')
router.register(r'points', PointsView, basename='points')

# content views
router.register(r'blog', BlogView, basename='blog')
router.register(r'faq', FaqView, basename='faq')
router.register(r'notification', NotificationView, basename='notification')
router.register(r'questions', QuestionsView, basename='questions')
router.register(r'image', ImageView, basename='image')


# core views
router.register(r'transaction', TransactionView, basename='transaction')
router.register(r'wallets', WalletsView, basename='wallets')

# orders views
router.register(r'orders', OrderView, basename='orders')
router.register(r'orders_status', OrderstatusView, basename='orders_status')
router.register(r'refund', RefundView, basename='refuld')

# payments views
router.register(r'currency', CurrencyView, basename='currency')
router.register(r'paymentaccount', PaymentaccountView, basename='paymentaccount')

# product views
router.register(r'attribute', AttributeView, basename='attribute')
router.register(r'attribute_value', AttributevalueView, basename='attribute_value')
router.register(r'compare', CompareView, basename='compare')
router.register(r'compare_items', CompareitemView, basename='compare_items')
router.register(r'category', CategoryView, basename='category')
router.register(r'product', ProductView, basename='product')
router.register(r'review', ReviewView, basename='review')
router.register(r'store', StoreView, basename='store')
router.register(r'tags', TagsView, basename='tags')
router.register(r'variantion', VariationView, basename='variantion')



urlpatterns = [
    path("", include(router.urls)),
]
