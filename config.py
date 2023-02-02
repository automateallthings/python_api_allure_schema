# Account
GET_ACCOUNT_DETAILS = '/api/accounts/accountId'
POST_CREATE_NEW_ACCOUNT = '/api/accounts'

# Agreement
GET_AGREEMENT_BY_ID = '/api/agreements/agreementId'

# Audit
GET_PASS_SUBSCRIPTION_BY_ACCOUNT_PRODUCT_ID = '/api/Audit/subscriptions/accountProductId'

# DataImport
POST_PASS_SUBSCRIPTION = '/api/DataImport/pass-subscriptions'
POST_DATA_BOOKING = '/api/DataImport/pass-subscriptions'

# domain
GET_PASS_AVAILABILITIES_BY_ACCOUNT_ID = '/api/domain/accountId/subscriptions/pass-availabilities'
GET_POST_SUBSCRIPTIONS_BY_ACCOUNT_ID = '/api/domain/accountId/subscriptions'  # Querying by bookingID "?bookingId=bookingId" for get
PUT_ADD_PASS_BOOKING_BY_ACCOUNT_ID_ACCOUNT_PRODUCT = '/api/domain/accountId/subscriptions/accountProductId/booking'
DELETE_BOOKING_BY_ACCOUNT_ID_ACCOUNT_PRODUCT_BOOKING_ID = '/api/domain/accountId/subscriptions/accountProductId/booking/bookingId'
PUT_UPDATE_ACCOUNT_USERS_BY_ACCOUNT_ID = '/api/domain/accountId/subscriptions/account-users'
DELETE_PASS_SUBSCRIPTION_BY_ACCOUNT_ID_ACCOUNT_PRODUCT_ID = '/api/domain/accountId/subscriptions/accountProductId'

# Product
GET_LIST_PRODUCT_BY_ACCOUNT_ID = '/api/accounts/accountId/products'

# Recommendation
GET_RECOMMENDATIONS_BY_ACCOUNT_ID = '/api/domain/accountId/recommendations'
PUT_RECOMMENDATIONS_BY_ACCOUNT_ID = '/api/domain/recommendations'

# Relationship
GET_POST_RELATIONSHIP_BY_ACCOUNT_ID = '/api/accounts/accountId/relationships'
GET_TYPE_OF_RELATIONSHIPS = '/api/relationships/types'

# Share
GET_POST_SHARE_BY_ACCOUNT_ID = '/api/accounts/accountId/shares'
DELETE_SHARE_BY_ACCOUNT_ID_SHARE_ID = '/api/accounts/accountId/shares/shareId'
