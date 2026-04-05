import requests
from django.conf import settings
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

# Step 1: Authenticate and get auth token
def get_auth_token():
    url = f"{settings.PAYMOB_BASE_URL}/auth/tokens"
    payload = {"api_key": settings.PAYMOB_API_KEY}
    r = requests.post(url, json=payload)
    r.raise_for_status()
    return r.json()["token"]

# Step 2: Create an order
def create_order(auth_token, amount_cents):
    url = f"{settings.PAYMOB_BASE_URL}/ecommerce/orders"
    payload = {
        "auth_token": auth_token,
        "delivery_needed": "false",
        "amount_cents": str(amount_cents),
        "currency": "EGP",
        "items": []
    }
    r = requests.post(url, json=payload)
    r.raise_for_status()
    return r.json()["id"]

# Step 3: Get payment key
def get_payment_key(auth_token, order_id, amount_cents, billing_data):
    url = f"{settings.PAYMOB_BASE_URL}/acceptance/payment_keys"
    payload = {
        "auth_token": auth_token,
        "amount_cents": str(amount_cents),
        "expiration": 3600,
        "order_id": order_id,
        "billing_data": billing_data,
        "currency": "EGP",
        "integration_id": settings.PAYMOB_INTEGRATION_ID
    }
    r = requests.post(url, json=payload)
    r.raise_for_status()
    return r.json()["token"]

# Step 4: Start payment
def start_payment(request):
    try:
        amount_cents = 10000  # 100 EGP
        billing_data = {
            "apartment": "NA",
            "email": "customer@example.com",
            "floor": "NA",
            "first_name": "John",
            "street": "NA",
            "building": "NA",
            "phone_number": "+201000000000",
            "shipping_method": "NA",
            "postal_code": "NA",
            "city": "Cairo",
            "country": "EG",
            "last_name": "Doe",
            "state": "NA"
        }

        auth_token = get_auth_token()
        order_id = create_order(auth_token, amount_cents)
        payment_token = get_payment_key(auth_token, order_id, amount_cents, billing_data)

        iframe_url = f"https://accept.paymob.com/api/acceptance/iframes/{settings.PAYMOB_IFRAME_ID}?payment_token={payment_token}"
        return redirect(iframe_url)

    except requests.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)

# Step 5: Callback after payment
@csrf_exempt
def payment_callback(request):
    # Paymob will send POST data here
    data = request.POST.dict()
    # TODO: Verify HMAC signature from Paymob for security
    return HttpResponse("Payment callback received")
