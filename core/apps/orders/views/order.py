from typing import Any

from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from ..models import OrderModel, OrderstatusModel
from ..serializers.order import (
    CreateOrderSerializer,
    CreateOrderstatusSerializer,
    ListOrderSerializer,
    ListOrderstatusSerializer,
    RetrieveOrderSerializer,
    RetrieveOrderstatusSerializer,
)

from core.apps.product.models import ProductModel
from core.apps.address.models import AddressModel




@extend_schema(tags=["OrderStatus"])
class OrderstatusView(BaseViewSetMixin, ModelViewSet):
    queryset = OrderstatusModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListOrderstatusSerializer
            case "retrieve":
                return RetrieveOrderstatusSerializer
            case "create":
                return CreateOrderstatusSerializer
            case _:
                return ListOrderstatusSerializer

    def get_permissions(self) -> Any:
        perms = [AllowAny]  
        self.permission_classes = perms
        return super().get_permissions()



@extend_schema(tags=["Order"])
class OrderView(BaseViewSetMixin, ModelViewSet):
    queryset = OrderModel.objects.all()

    def get_serializer_class(self) -> Any:
        # Har bir action uchun mos serializerni qaytarish
        if self.action == "list":
            return ListOrderSerializer
        elif self.action == "retrieve":
            return RetrieveOrderSerializer
        elif self.action == "create":
            return CreateOrderSerializer
        else:
            return ListOrderSerializer

    def get_permissions(self) -> Any:
        # Har bir action uchun kerakli ruxsatlar
        if self.action in ["create", "update", "destroy"]:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    def perform_create(self, serializer):
        order = serializer.save()

        products_data = self.request.data.get("products", [])
        if products_data:
            products = ProductModel.objects.filter(id__in=products_data)
            if products.exists():
                order.products.set(products) 
            else:
                raise Exception("Mahsulotlar topilmadi!")
        else:
            raise Exception("Mahsulotlar ro‘yxati bo‘sh.")

        billing_address_id = self.request.data.get("billing_address_id", None)
        if billing_address_id:
            try:
                billing_address = AddressModel.objects.get(id=billing_address_id)
                order.billing_address = billing_address
            except AddressModel.DoesNotExist:
                raise Exception("Billing address not found.")

        shipping_address_id = self.request.data.get("shipping_address_id", None)
        if shipping_address_id:
            try:
                shipping_address = AddressModel.objects.get(id=shipping_address_id)
                order.shipping_address = shipping_address
            except AddressModel.DoesNotExist:
                raise Exception("Shipping address not found.")

        parent_id = self.request.data.get("parent_id", None)
        if parent_id:
            try:
                parent_order = OrderModel.objects.get(id=parent_id)
                order.parent = parent_order
            except OrderModel.DoesNotExist:
                raise Exception("Parent order not found.")

        order_number = self.request.data.get("order_number", None)
        if order_number:
            order.order_number = order_number

        deleted_at = self.request.data.get("deleted_at", None)
        if deleted_at:
            order.deleted_at = deleted_at

        invoice_url = self.request.data.get("invoice_url", None)
        if invoice_url:
            order.invoice_url = invoice_url

        order.tax_total = self.request.data.get("tax_total", 0)
        order.shipping_total = self.request.data.get("shipping_total", 0)
        order.points_amount = self.request.data.get("points_amount", 0)
        order.wallet_balance = self.request.data.get("wallet_balance", 0)
        order.amount = self.request.data.get("amount", 0)
        order.total = self.request.data.get("total", 0)
        order.coupon_total_discount = self.request.data.get("coupon_total_discount", 0)
        order.payment_method = self.request.data.get("payment_method", "")
        order.payment_status = self.request.data.get("payment_status", "")
        order.store_id = self.request.data.get("store_id", None)
        order.consumer_id = self.request.data.get("consumer_id", None)
        order.order_status_id = self.request.data.get("order_status_id", None)
        order.coupon_id = self.request.data.get("coupon_id", None)
        order.created_by_id = self.request.data.get("created_by_id", None)
        order.status = self.request.data.get("status", 1)
        order.delivered_at = self.request.data.get("delivered_at", None)
        order.created_at = self.request.data.get("created_at", None)
        order.updated_at = self.request.data.get("updated_at", None)
        order.state = self.request.data.get("state", 1)

        order.save()

        return order
