#Membership URL
BASE_URI = 'https://app-membershipapi-test.azurewebsites.net'
#BASE_URI = 'https://app-membershipapi-qa.azurewebsites.net'

#RestStop Membership URL
MEM_RS_TEST_URL = 'https://apis.test.inspirato.com/membership/apex-beta'
MEM_RS_QA_URL = 'https://apis.qa.inspirato.com/membership/apex-beta'

#Authentication URL
AUTH_URL = 'https://test-signin.inspirato.com/oauth2/default/v1/token'

#Account
GET_ACCOUNT_DETAILS = '/api/accounts/accountId'
POST_CREATE_NEW_ACCOUNT = '/api/accounts'

#Agreement
GET_AGREEMENT_BY_ID = '/api/agreements/agreementId'

#Audit
GET_PASS_SUBSCRIPTION_BY_ACCOUNT_PRODUCT_ID = '/api/Audit/subscriptions/accountProductId'

#DataImport
POST_PASS_SUBSCRIPTION = '/api/DataImport/pass-subscriptions'
POST_DATA_BOOKING = '/api/DataImport/pass-subscriptions'

#Membership
GET_PASS_AVAILABILITIES_BY_ACCOUNT_ID = '/api/Membership/accountId/subscriptions/pass-availabilities'
GET_POST_SUBSCRIPTIONS_BY_ACCOUNT_ID = '/api/Membership/accountId/subscriptions' #Quering by bookingID "?bookingId=bookingId" for get
PUT_ADD_PASS_BOOKING_BY_ACCOUNT_ID_ACCOUNT_PRODUCT = '/api/Membership/accountId/subscriptions/accountProductId/booking'
DELETE_BOOKING_BY_ACCOUNT_ID_ACCOUNT_PRODUCT_BOOKING_ID = '/api/Membership/accountId/subscriptions/accountProductId/booking/bookingId'
PUT_UPDATE_ACCOUNT_USERS_BY_ACCOUNT_ID = '/api/Membership/accountId/subscriptions/account-users'
DELETE_PASS_SUBSCRIPTION_BY_ACCOUNT_ID_ACCOUNT_PRODUCT_ID = '/api/Membership/accountId/subscriptions/accountProductId'

#Product
GET_LIST_PRODUCT_BY_ACCOUNT_ID = '/api/accounts/accountId/products'

#Recomendation
GET_RECOMMENDATIONS_BY_ACCOUNT_ID = '/api/Membership/accountId/recommendations'
PUT_RECOMMENDATIONS_BY_ACCOUNT_ID = '/api/Membership/recommendations'

#Relationship
GET_POST_RELATIONSHIP_BY_ACCOUNT_ID = '/api/accounts/accountId/relationships'
GET_TYPE_OF_RELATIONSHIPS = '/api/relationships/types'

#Share
GET_POST_SHARE_BY_ACCOUNT_ID = '/api/accounts/accountId/shares'
DELETE_SHARE_BY_ACCOUNT_ID_SHARE_ID = '/api/accounts/accountId/shares/shareId'
