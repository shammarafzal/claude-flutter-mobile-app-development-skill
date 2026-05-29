# API, Laravel, Firebase, and Local Storage

## REST API rules

Never call HTTP APIs directly from widgets.

Use:

```text
RemoteDataSource -> RepositoryImpl -> UseCase -> Bloc/Cubit/ViewModel -> Page
```

## Dio API client

Use a central client for:

- base URL
- auth header
- timeout
- interceptors
- refresh token logic
- logging in debug only
- error mapping

See `templates/dio_api_client.dart`.

## Laravel API conventions

Common Flutter + Laravel backend setup:

- Laravel Sanctum/JWT/Passport for auth
- JSON API responses
- Pagination for lists
- File upload endpoints
- Push notification token endpoint
- Payment intent/order endpoint
- Admin dashboard controls data, Flutter consumes APIs

Recommended response shape:

```json
{
  "success": true,
  "message": "Request completed",
  "data": {}
}
```

Recommended error shape:

```json
{
  "success": false,
  "message": "Validation failed",
  "errors": {
    "email": ["The email field is required."]
  }
}
```

## Auth token handling

- Store access token securely when needed.
- Refresh tokens via backend endpoint.
- Clear local auth state on 401/invalid session.
- Do not expose backend admin credentials.

## Firebase rules

Use Firebase for:

- Auth
- Firestore/Realtime Database
- FCM push notifications
- Crashlytics
- Analytics
- Remote Config

Do not put Firebase Admin SDK credentials or service account keys in Flutter.

## Payments

Never store payment secret keys in Flutter.

Correct flow:

1. Flutter calls backend: create payment/order.
2. Backend calls Stripe/PayPal/payment provider.
3. Backend returns a client-safe token/session.
4. Flutter confirms payment.
5. Backend verifies webhook.
6. Backend updates order status.

## Offline/cache rules

Use cache when:

- Lists are repeatedly opened
- App must work during poor connectivity
- UX benefits from instant loading

Options:

- `shared_preferences`: small key-value settings
- `flutter_secure_storage`: sensitive tokens
- `hive`/`isar`: local objects
- `drift`: relational local database
