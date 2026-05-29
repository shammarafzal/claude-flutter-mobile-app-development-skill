# Publishing Checklist

## Android

- [ ] App name updated
- [ ] Package/application ID updated
- [ ] App icon added
- [ ] Adaptive icon configured
- [ ] Splash screen configured
- [ ] Signing key generated and stored safely
- [ ] `key.properties` excluded from public repos
- [ ] Release build tested on real Android device
- [ ] App Bundle generated with `flutter build appbundle --release`
- [ ] Privacy policy URL ready
- [ ] Store screenshots ready
- [ ] Play Store Data Safety form completed
- [ ] Permissions reviewed and justified
- [ ] Version code/version name updated

## iOS

- [ ] Bundle ID updated
- [ ] Apple Developer account available
- [ ] Signing/provisioning configured
- [ ] App icon added
- [ ] Launch screen configured
- [ ] Release tested on real iPhone
- [ ] Archive created in Xcode
- [ ] Uploaded to App Store Connect
- [ ] Privacy nutrition labels completed
- [ ] Screenshots prepared
- [ ] Version/build updated

## Production app readiness

- [ ] API base URL points to production
- [ ] Debug banners removed
- [ ] Test credentials removed
- [ ] Crash reporting configured
- [ ] Analytics configured if needed
- [ ] No secrets in client code
- [ ] No verbose logs in release
- [ ] Loading/error/empty states tested
- [ ] Offline/no-internet state tested
- [ ] Authentication expiration tested
- [ ] Push notification permission flow tested
- [ ] Deep links tested if used
