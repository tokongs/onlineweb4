# Make sure these exist in settings if they are to be used.
class StripeKey:
    ARRKOM = 'arrkom'
    PROKOM = 'prokom'
    TRIKOM = 'trikom'
    FAGKOM = 'fagkom'

    ALL_TYPES = (ARRKOM, PROKOM, TRIKOM, FAGKOM,)
    ALL_CHOICES = [(t, t) for t in ALL_TYPES]


class VatTypeSale:
    NONE = 'NONE'
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    RAW_FISH = 'RAW_FISH'
    LOW = 'LOW'
    EXEMPT_IMPORT_EXPORT = 'EXEMPT_IMPORT_EXPORT'
    EXEMPT = 'EXEMPT'
    OUTSIDE = 'OUTSIDE'
    EXEMPT_REVERSE = 'EXEMPT_REVERSE'

    ALL_TYPES = (
        NONE,
        HIGH,
        MEDIUM,
        RAW_FISH,
        LOW,
        EXEMPT_IMPORT_EXPORT,
        EXEMPT,
        OUTSIDE,
        EXEMPT_REVERSE,
    )
    ALL_CHOICES = [(t, t) for t in ALL_TYPES]


class VatTypePurchase:
    NONE = 'NONE'
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    RAW_FISH = 'RAW_FISH'
    LOW = 'LOW'
    EXEMPT_IMPORT_EXPORT = 'EXEMPT_IMPORT_EXPORT'
    HIGH_DIRECT = 'HIGH_DIRECT'
    HIGH_BASIS = 'HIGH_BASIS'
    MEDIUM_DIRECT = 'MEDIUM_DIRECT'
    MEDIUM_BASIS = 'MEDIUM_BASIS'
    NONE_IMPORT_BASIS = 'NONE_IMPORT_BASIS'
    HIGH_IMPORT_DEDUCTIBLE = 'HIGH_IMPORT_DEDUCTIBLE'
    HIGH_IMPORT_NONDEDUCTIBLE = 'HIGH_IMPORT_NONDEDUCTIBLE'
    MEDIUM_IMPORT_DEDUCTIBLE = 'MEDIUM_IMPORT_DEDUCTIBLE'
    MEDIUM_IMPORT_NONDEDUCTIBLE = 'MEDIUM_IMPORT_NONDEDUCTIBLE'
    HIGH_FOREIGN_SERVICE_DEDUCTIBLE = 'HIGH_FOREIGN_SERVICE_DEDUCTIBLE'
    HIGH_FOREIGN_SERVICE_NONDEDUCTIBLE = 'HIGH_FOREIGN_SERVICE_NONDEDUCTIBLE'
    LOW_FOREIGN_SERVICE_DEDUCTIBLE = 'LOW_FOREIGN_SERVICE_DEDUCTIBLE'
    LOW_FOREIGN_SERVICE_NONDEDUCTIBLE = 'LOW_FOREIGN_SERVICE_NONDEDUCTIBLE'
    HIGH_PURCHASE_OF_EMISSIONSTRADING_OR_GOLD_DEDUCTIBLE = 'HIGH_PURCHASE_OF_EMISSIONSTRADING_OR_GOLD_DEDUCTIBLE'
    HIGH_PURCHASE_OF_EMISSIONSTRADING_OR_GOLD_NONDEDUCTIBLE = 'HIGH_PURCHASE_OF_EMISSIONSTRADING_OR_GOLD_NONDEDUCTIBLE'

    ALL_TYPES = (
        NONE,
        HIGH,
        MEDIUM,
        RAW_FISH,
        LOW,
        EXEMPT_IMPORT_EXPORT,
        HIGH_DIRECT,
        HIGH_BASIS,
        MEDIUM_DIRECT,
        MEDIUM_BASIS,
        NONE_IMPORT_BASIS,
        HIGH_IMPORT_DEDUCTIBLE,
        HIGH_IMPORT_NONDEDUCTIBLE,
        MEDIUM_IMPORT_DEDUCTIBLE,
        MEDIUM_IMPORT_NONDEDUCTIBLE,
        HIGH_FOREIGN_SERVICE_DEDUCTIBLE,
        HIGH_FOREIGN_SERVICE_NONDEDUCTIBLE,
        LOW_FOREIGN_SERVICE_DEDUCTIBLE,
        LOW_FOREIGN_SERVICE_NONDEDUCTIBLE,
        HIGH_PURCHASE_OF_EMISSIONSTRADING_OR_GOLD_DEDUCTIBLE,
        HIGH_PURCHASE_OF_EMISSIONSTRADING_OR_GOLD_NONDEDUCTIBLE,
    )
    ALL_CHOICES = [(t, t) for t in ALL_TYPES]


class FikenAccount:
    ARRKOM = '1960:10003'
    PROKOM = '1960:10002'
    TRIKOM = '1960:10001'
    FAGKOM = '1960:10004'

    ALL_ACCOUNTS = (ARRKOM, PROKOM, TRIKOM, FAGKOM,)
    ALL_CHOICES = [(a, a) for a in ALL_ACCOUNTS]


class FikenSaleKind:
    CASH_SALE = 'CASH_SALE'
    INVOICE = 'INVOICE'
    EXTERNAL_INVOICE = 'EXTERNAL_INVOICE'

    ALL_KINDS = (CASH_SALE, INVOICE, EXTERNAL_INVOICE,)
    ALL_CHOICES = [(k, k) for k in ALL_KINDS]


class TransactionType:
    KIOSK = 'kiosk'
    WEB_SHOP = 'webshop'
    EVENT = 'event'

    ALL_TYPES = (KIOSK, WEB_SHOP, EVENT,)
    ALL_CHOICES = [(t, t) for t in ALL_TYPES]