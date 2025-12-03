---
id: HASKI-REQ-0028
title: LTI-basierte Moodle-Integration mit Authentifizierung
type: Interface
status: Implemented
source_id: SyRS-INT-003
links:
  stories:
    [
      "HASKI-RAK/HASKI-Backend#19",
      "HASKI-RAK/HASKI-Frontend#138",
      "HASKI-RAK/HASKI-Backend#42",
      "HASKI-RAK/HASKI-Frontend#83",
      "HASKI-RAK/HASKI-Frontend#146",
    ]
  parents: ["SyRS-INT-003"]
  tests:
    - path: "frontend/src/components/LoginForm/LoginForm.test.tsx"
      name: "Test LoginForm"
    - path: "backend/tests/unit/lti/test_CookieServiceFlask.py"
      name: "CookieServiceFlask::test_set_cookie"
    - path: "backend/tests/unit/lti/test_CookieServiceFlask.py"
      name: "CookieServiceFlask::test_delete_cookie"
    - path: "backend/tests/unit/lti/test_cryptorandom.py"
      name: "CryptoRandom::test_getRandom"
    - path: "frontend/src/pages/Login/Login.test.tsx"
      name: "Login Page"
    - path: "frontend/src/services/auth/fetchLogout.test.tsx"
      name: "fetchLogout"
    - path: "frontend/src/services/auth/fetchUser.test.tsx"
      name: "fetchUser"
    - path: "frontend/src/services/auth/postLogin.test.tsx"
      name: "postLogin"
    - path: "frontend/src/services/auth/fetchRedirectMoodleLogin.test.tsx"
      name: "fetchRedirectMoodleLogin"
    - path: "frontend/src/services/auth/postLoginCredentials.test.tsx"
      name: "getLoginStatus"
    - path: "frontend/src/services/AuthContext/AuthContext.test.tsx"
      name: "Test Authcontext"
    - path: "frontend/src/services/AuthProvider/AuthProvider.test.tsx"
      name: "Test AuthProvider"
    - path: "backend/tests/unit/test_auth.py"
      name: "TestAuthorizeDecorator::test_authorized_user"
    - path: "backend/tests/unit/test_auth.py"
      name: "TestAuthorizeDecorator::test_unauthorized_user"
    - path: "backend/tests/unit/lti/test_JWTKeyManagement.py"
      name: "TestJWTKeyManagement::test_get_unverified_header"
    - path: "backend/tests/unit/lti/test_JWTKeyManagement.py"
      name: "TestJWTKeyManagement::test_fail_get_unverified_header"
    - path: "backend/tests/unit/lti/test_JWTKeyManagement.py"
      name: "TestJWTKeyManagement::test_load_jwt"
    - path: "backend/tests/unit/lti/test_JWTKeyManagement.py"
      name: "TestJWTKeyManagement::test_sign_verify_jwt"
    - path: "backend/tests/unit/lti/test_JWTKeyManagement.py"
      name: "TestJWTKeyManagement::test_no_key_sign_verify_jwt"
    - path: "backend/tests/unit/lti/test_JWTKeyManagement.py"
      name: "TestJWTKeyManagement::test_fail_verify_jwt"
    - path: "backend/tests/unit/lti/test_JWTKeyManagement.py"
      name: "TestJWTKeyManagement::test_construct_jwt"
    - path: "backend/tests/unit/lti/test_JWTKeyManagement.py"
      name: "TestJWTKeyManagement::test_no_public_key_location"
    - path: "backend/tests/unit/lti/test_JWTKeyManagement.py"
      name: "TestJWTKeyManagement::test_no_private_key_location"
    - path: "backend/tests/unit/lti/test_JWTKeyManagement.py"
      name: "TestJWTKeyManagement::test_nonce_jwt"
    - path: "backend/tests/unit/lti/test_JWTKeyManagement.py"
      name: "TestJWTKeyManagement::test_state_jwt"
    - path: "backend/tests/unit/lti/test_OIDCLoginFlask.py"
      name: "TestOIDCLoginFlask::test_tool_config_decode_platform"
    - path: "backend/tests/unit/lti/test_OIDCLoginFlask.py"
      name: "TestOIDCLoginFlask::test_no_platform"
    - path: "backend/tests/unit/lti/test_OIDCLoginFlask.py"
      name: "TestOIDCLoginFlask::test_check_params_successful"
    - path: "backend/tests/unit/lti/test_OIDCLoginFlask.py"
      name: "TestOIDCLoginFlask::test_check_params_missing_iss"
    - path: "backend/tests/unit/lti/test_OIDCLoginFlask.py"
      name: "TestOIDCLoginFlask::test_check_params_missing_platform"
    - path: "backend/tests/unit/lti/test_OIDCLoginFlask.py"
      name: "TestOIDCLoginFlask::test_check_params_wrong_target_link_uri"
    - path: "backend/tests/unit/lti/test_OIDCLoginFlask.py"
      name: "TestOIDCLoginFlask::test_prod_no_https"
    - path: "backend/tests/unit/lti/test_OIDCLoginFlask.py"
      name: "TestOIDCLoginFlask::test_verify_state_successful"
    - path: "backend/tests/unit/lti/test_OIDCLoginFlask.py"
      name: "TestOIDCLoginFlask::test_verify_state_invalid_jwt"
    - path: "backend/tests/unit/lti/test_OIDCLoginFlask.py"
      name: "TestOIDCLoginFlask::test_verify_state_invalid_payload"
    - path: "backend/tests/unit/lti/test_OIDCLoginFlask.py"
      name: "TestOIDCLoginFlask::test_verify_id_token_error_in_form"
    - path: "backend/tests/unit/lti/test_OIDCLoginFlask.py"
      name: "TestOIDCLoginFlask::test_verify_id_token_unverified_header_fail"
    - path: "backend/tests/unit/lti/test_OIDCLoginFlask.py"
      name: "TestOIDCLoginFlask::test_verify_id_token_successful"
    - path: "backend/tests/unit/lti/test_OIDCLoginFlask.py"
      name: "TestOIDCLoginFlask::test_lti_launch_from_id_token_user_does_not_exist_in_db"
    - path: "backend/tests/unit/lti/test_OIDCLoginFlask.py"
      name: "TestOIDCLoginFlask::test_lti_launch_from_id_token_user_exists_in_db"
    - path: "backend/tests/unit/lti/test_OIDCLoginFlask.py"
      name: "TestOIDCLoginFlask::test_get_cookie_expiration_successful"
    - path: "backend/tests/unit/lti/test_OIDCLoginFlask.py"
      name: "TestOIDCLoginFlask::test_lti_launch_from_id_token_user_does_not_exist_in_db_role_course_creator"
    - path: "backend/tests/unit/lti/test_OIDCLoginFlask.py"
      name: "TestOIDCLoginFlask::test_get_logout"
    - path: "backend/tests/unit/lti/test_Roles.py"
      name: "TestRoles::test_lti_roles"
    - path: "backend/tests/unit/lti/test_Roles.py"
      name: "TestRoles::test_lti_permissions"
    - path: "backend/tests/unit/lti/test_Roles.py"
      name: "TestRoleMapper::test_map_role"
    - path: "backend/tests/unit/lti/test_Roles.py"
      name: "TestRoleMapper::test_constructor"
    - path: "backend/tests/unit/lti/test_Roles.py"
      name: "TestRoleMapper::test_get_role"
    - path: "backend/tests/unit/lti/test_Roles.py"
      name: "TestRoleMapper::test_get_permissions"
    - path: "backend/tests/unit/lti/test_SessionServiceFlask.py"
      name: "TestSessionClass::test_constructor"
    - path: "backend/tests/unit/lti/test_SessionServiceFlask.py"
      name: "TestSessionClass::test_setitem"
    - path: "backend/tests/unit/lti/test_SessionServiceFlask.py"
      name: "TestSessionClass::test_delitem"
    - path: "backend/tests/unit/lti/test_SessionServiceFlask.py"
      name: "TestSessionClass::test_getitem"
    - path: "backend/tests/unit/lti/test_SessionServiceFlask.py"
      name: "TestSessionModule::test_set_state_jwt"
    - path: "backend/tests/unit/lti/test_SessionServiceFlask.py"
      name: "TestSessionModule::test_set"
    - path: "backend/tests/unit/lti/test_SessionServiceFlask.py"
      name: "TestSessionModule::test_get"
    - path: "backend/tests/unit/lti/test_SessionServiceFlask.py"
      name: "TestSessionModule::test_check_expiration"
    - path: "backend/tests/unit/lti/test_cryptorandom.py"
      name: "test_getrandbits"
    - path: "backend/tests/unit/lti/test_cryptorandom.py"
      name: "test_getrandbytes"
    - path: "backend/tests/unit/lti/test_cryptorandom.py"
      name: "test_createuniqueid"
    - path: "backend/tests/unit/lti/test_cryptorandom.py"
      name: "test_createuniqueidbase64"
    - path: "backend/tests/unit/lti/test_cryptorandom.py"
      name: "test_getrandomstring"
    - path: "backend/tests/unit/lti/test_cryptorandom.py"
      name: "test_getrandomstringbase64"
---

## Beschreibung

Das System **shall** über standardisierte LTI 1.3 Schnittstellen (Learning Tools Interoperability) eine nahtlose Integration mit Moodle ermöglichen. Die LTI-Verbindung **shall** für die Authentifizierung und Autorisierung von Nutzern verwendet werden und **shall** nur autorisierte Moodle-Plattformen akzeptieren.

Die LTI-Integration **shall** folgende Funktionalitäten bereitstellen:

- Authentifizierung von Nutzern über LTI-Launch aus Moodle
- Sicherer Datenaustausch über JWT-basierte Token
- Cookie-basiertes Session-Management für authentifizierte Nutzer
- Zugriffskontrolle auf API-Endpunkte basierend auf LTI-Authentifizierung
- Ablehnung von nicht autorisierten Nutzern und Plattformen

## Akzeptanzkriterien

### Funktionale Anforderungen

- [ ] Das System implementiert LTI 1.3 Verbindung für Authentifizierung in HASKI mittels pylti-Bibliothek
- [ ] Die LTI-Verbindung ist als API-Endpunkt implementiert
- [ ] LTI setzt Cookies korrekt für authentifizierte Sessions
- [ ] LTI akzeptiert nur die spezifizierte Moodle-Plattform (keine anderen Plattformen)
- [ ] LTI kann Nutzer ablehnen, die nicht berechtigt sind, HASKI zu betreten
- [ ] Ein Authentifizierungs-Decorator ist über API-Endpunkten implementiert
- [ ] Das System prüft Zugriffsberechtigung und implementiert 401 Unauthorized Fehler
- [ ] LTI-Konfiguration wird aus Environment-Datei geladen
- [ ] Frontend ist mit LTI verbunden und konfiguriert
- [ ] HASKI agiert als Plattform zur Integration von Moodle-Aktivitäten

### Qualitätsanforderungen

- [ ] Code entspricht Python-Standard (Linting bestanden)
- [ ] Alle Pytest-Tests bestehen
- [ ] Namensgebung ist aussagekräftig und konsistent
- [ ] Unit Test Coverage > 90%
- [ ] Dokumentation der LTI-Integration ist erstellt
- [ ] UML-Klassendiagramme und Komponentendiagramme sind aktualisiert

### Sicherheitsanforderungen

- [ ] Session Management ist sicher implementiert
- [ ] JWT-Token werden korrekt validiert
- [ ] Nur autorisierte Moodle-Instanzen werden akzeptiert
- [ ] API-Endpunkte sind durch LTI-Authentifizierung geschützt

## Rationale

Primary implementation: GitHub issue GH-19: "[Technical] Implement LTI Connection for Moodle"

Related work:

- GH-138 (Frontend): LTI connection and configuration on frontend side
- GH-42 (Backend): API access control implementation using LTI authentication
- GH-83 (Frontend): HASKI as platform to integrate Moodle activities, session management
- GH-146 (Frontend): LTI registration in webapp (open issue for future enhancements)

Derived from system requirement SyRS-INT-003 and stakeholder requirement StRS-121.

Die LTI-Integration ermöglicht die nahtlose Einbettung von HASKI in bestehende Moodle-Infrastrukturen und reduziert Implementierungshürden für Hochschulen.

## Hinweise

- Primary issue: [GH-19](https://github.com/HASKI-RAK/HASKI-Backend/issues/19) - Implementiert LTI 1.3 Verbindung mit pylti-Bibliothek
- Related issues:
  - [GH-138](https://github.com/HASKI-RAK/HASKI-Frontend/issues/138) - Frontend LTI Konfiguration
  - [GH-42](https://github.com/HASKI-RAK/HASKI-Backend/issues/42) - API Access Control mit LTI
  - [GH-83](https://github.com/HASKI-RAK/HASKI-Frontend/issues/83) - HASKI als Plattform
  - [GH-146](https://github.com/HASKI-RAK/HASKI-Frontend/issues/146) - LTI Registration (offen)
- Backend test `backend/tests/unit/lti/test_cryptorandom.py::test_getRandom` deckt die kryptographische Zufallszahlenerzeugung für LTI-Nonce und State ab (GH-19).
- Technische Bibliothek: [pylti1.3](https://github.com/dmitry-viskov/pylti1.3)
- Standard: IMS Global Learning Consortium – LTI 1.3 Standard
- LTI-Konfiguration erfolgt über .env-Datei (siehe GH-64)
- Authentifizierung erfolgt über Cookie-basiertes Session-Management
- API-Endpunkte verwenden Decorator-Pattern für Zugriffskontrolle
