from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PAGES = [
    {
        "separator": True,
        "items": [
            {
                "title": _("Home page"),
                "icon": "home",  # Google Material Icons Home icon
                "link": reverse_lazy("admin:index"),
            }
        ],
    },
    {
        "title": _("Auth"),
        "separator": True,
        "collapsible": True,
        "items": [
            {
                "title": _("Users"),
                "icon": "group",  # Google Material Icons Group (Users) icon
                "link": reverse_lazy("admin:accounts_user_changelist"),
            },
            {
                "title": _("Role"),
                "icon": "group",  # Google Material Icons Group (Users) icon
                "link": reverse_lazy("admin:accounts_role_changelist"),
            },
            {
                "title": _("Pivot"),
                "icon": "swap_horiz",  # Google Material Icons Group (Users) icon
                "link": reverse_lazy("admin:accounts_pivot_changelist"),
            },

        ],
    },
    {
        "title": _("Address"),
        "separator": True,
        "collapsible": True,
        "items": [
            {
                "title": _("Address"),
                "icon": "place",  # Google Material Icons Place (Address) icon
                "link": reverse_lazy("admin:address_addressmodel_changelist"),
            },
            {
                "title": _("Country"),
                "icon": "flag",  # Google Material Icons Flag icon
                "link": reverse_lazy("admin:address_countrymodel_changelist"),
            },
            {
                "title": _("State"),
                "icon": "location_on",  # Google Material Icons Location On (State) icon
                "link": reverse_lazy("admin:address_statemodel_changelist"),
            },
        ],
    },
    {
        "title": _("Cart"),
        "separator": True,
        "collapsible": True,
        "items": [
            {
                "title": _("Cart"),
                "icon": "shopping_cart",  # Google Material Icons Shopping Cart icon
                "link": reverse_lazy("admin:cart_cartmodel_changelist"),
            },
            {
                "title": _("Coupon"),
                "icon": "local_offer",  # Google Material Icons Local Offer (Coupon) icon
                "link": reverse_lazy("admin:cart_couponmodel_changelist"),
            },
            {
                "title": _("Points"),
                "icon": "stars",  # Google Material Icons Stars (Points) icon
                "link": reverse_lazy("admin:cart_pointsmodel_changelist"),
            },
            {
                "title": _("Wishlist"),
                "icon": "favorite",  # Google Material Icons Favorite (Wishlist) icon
                "link": reverse_lazy("admin:cart_wishlistmodel_changelist"),
            },
        ],
    },
    {
        "title": _("Content"),
        "separator": True,
        "collapsible": True,
        "items": [
            {
                "title": _("Blog"),
                "icon": "article",  # Google Material Icons Article (Blog) icon
                "link": reverse_lazy("admin:content_blogmodel_changelist"),
            },
            {
                "title": _("Faq"),
                "icon": "question_answer",  # Google Material Icons Question Answer (FAQ) icon
                "link": reverse_lazy("admin:content_faqmodel_changelist"),
            },
            {
                "title": _("Image"),
                "icon": "image",  # Google Material Icons Image icon
                "link": reverse_lazy("admin:content_imagemodel_changelist"),
            },
            {
                "title": _("Notification"),
                "icon": "notifications",  # Google Material Icons Notifications icon
                "link": reverse_lazy("admin:content_notificationmodel_changelist"),
            },
            {
                "title": _("Questions"),
                "icon": "help",  # Google Material Icons Help icon
                "link": reverse_lazy("admin:content_questionsmodel_changelist"),
            },
        ],
    },
    {
        "title": _("Core"),
        "separator": True,
        "collapsible": True,
        "items": [
            {
                "title": _("Transaction"),
                "icon": "account_balance",  # Google Material Icons Account Balance (Transaction) icon
                "link": reverse_lazy("admin:core_transactionmodel_changelist"),
            },
            {
                "title": _("Wallets"),
                "icon": "wallet",  # Google Material Icons Wallet icon
                "link": reverse_lazy("admin:core_walletsmodel_changelist"),
            },
        ],
    },
    {
        "title": _("Orders"),
        "separator": True,
        "collapsible": True,
        "items": [
            {
                "title": _("Order"),
                "icon": "assignment",  # Google Material Icons Assignment (Order) icon
                "link": reverse_lazy("admin:orders_ordermodel_changelist"),
            },
            {
                "title": _("Order Status"),
                "icon": "list_alt",  # Google Material Icons List Alt (Order Status) icon
                "link": reverse_lazy("admin:orders_orderstatusmodel_changelist"),
            },
            {
                "title": _("Refund"),
                "icon": "refund",  # Google Material Icons Refund icon
                "link": reverse_lazy("admin:orders_refundmodel_changelist"),
            },
        ],
    },
    {
        "title": _("Payments"),
        "separator": True,
        "collapsible": True,
        "items": [
            {
                "title": _("Currency"),
                "icon": "attach_money",  # Google Material Icons Attach Money (Currency) icon
                "link": reverse_lazy("admin:payments_currencymodel_changelist"),
            },
            {
                "title": _("Payments Accounts"),
                "icon": "credit_card",  # Google Material Icons Credit Card (Payments Accounts) icon
                "link": reverse_lazy("admin:payments_paymentaccountmodel_changelist"),
            },
        ],
    },
    {
        "title": _("Product"),
        "separator": True,
        "collapsible": True,
        "items": [
            {
                "title": _("Attribute"),
                "icon": "settings_input_component",  # Google Material Icons Settings Input Component (Attribute) icon
                "link": reverse_lazy("admin:product_attributemodel_changelist"),
            },
            {
                "title": _("Attribute Value"),
                "icon": "tune",  # Google Material Icons Tune (Attribute Value) icon
                "link": reverse_lazy("admin:product_attributevaluemodel_changelist"),
            },
            {
                "title": _("Category"),
                "icon": "category",  # Google Material Icons Category icon
                "link": reverse_lazy("admin:product_categorymodel_changelist"),
            },
            {
                "title": _("Compare"),
                "icon": "compare_arrows",  # Google Material Icons Compare Arrows icon
                "link": reverse_lazy("admin:product_comparemodel_changelist"),
            },
            {
                "title": _("Compare Item"),
                "icon": "shopping_basket",  # Google Material Icons Shopping Basket icon
                "link": reverse_lazy("admin:product_compareitemmodel_changelist"),
            },
            {
                "title": _("Product"),
                "icon": "inventory",  # Google Material Icons Inventory (Product) icon
                "link": reverse_lazy("admin:product_productmodel_changelist"),
            },
            {
                "title": _("Review"),
                "icon": "rate_review",  # Google Material Icons Rate Review icon
                "link": reverse_lazy("admin:product_reviewmodel_changelist"),
            },
            {
                "title": _("Store"),
                "icon": "store",  # Google Material Icons Store icon
                "link": reverse_lazy("admin:product_storemodel_changelist"),
            },
            {
                "title": _("Tags"),
                "icon": "label",  # Google Material Icons Label icon
                "link": reverse_lazy("admin:product_tagsmodel_changelist"),
            },
            {
                "title": _("Tax"),
                "icon": "local_taxi",  # Google Material Icons Local Taxi (Tax) icon
                "link": reverse_lazy("admin:product_taxmodel_changelist"),
            },
            {
                "title": _("Variation"),
                "icon": "flaky",  # Google Material Icons Flaky (Variation) icon
                "link": reverse_lazy("admin:product_variationmodel_changelist"),
            },
        ],
    },
]
