# Timed Backend

[![Build Status](https://travis-ci.org/adfinis-sygroup/timed-backend.svg?branch=master)](https://travis-ci.org/adfinis-sygroup/timed-backend)
[![Codecov](https://codecov.io/gh/adfinis-sygroup/timed-backend/branch/master/graph/badge.svg)](https://codecov.io/gh/adfinis-sygroup/timed-backend)
[![Pyup](https://pyup.io/repos/github/adfinis-sygroup/timed-backend/shield.svg)](https://pyup.io/account/repos/github/adfinis-sygroup/timed-backend/)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/adfinis-sygroup/timed-backend)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

Timed timetracking software REST API built with Django

## Installation

**Requirements**

- docker
- docker-compose

After installing and configuring those requirements, you should be able to run the following
commands to complete the installation:

Add the `timed.local` entries to your hosts file:
```bash
echo "127.0.0.1 timed.local" | sudo tee -a /etc/hosts
```

Then just start the docker-compose setup:
```bash
make start
```

This brings up complete local installation, including our [Timed Frontend](https://github.com/adfinis-sygroup/timed-frontend) project.

You can visit it at [http://timed.local](http://timed.local).

The API can be accessed at [http://timed.local/api/v1](http://timed.local/api/v1) and the admin interface at [http://timed.local/admin/](http://timed.local/admin/).

## Development

To get the application working locally for development, make sure to create a file `.env` with the following content:

```
ENV=dev
```

If you have existing users from the previous LDAP authentication, you want to add this line as well:

```
DJANGO_OIDC_USERNAME_CLAIM=preferred_username
```

## Configuration

Following options can be set as environment variables to configure Timed backend in documented [format](https://github.com/joke2k/django-environ#supported-types)
according to type.

| Parameter                                    | Description                                                                              | Default                                                      |
|----------------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| `DJANGO_ENV_FILE`                            | Path to setup environment vars in a file                                                 | .env                                                         |
| `DJANGO_DEBUG`                               | Boolean that turns on/off debug mode                                                     | False                                                        |
| `DJANGO_SECRET_KEY`                          | Secret key for cryptographic signing                                                     | not set (required)                                           |
| `DJANGO_ALLOWED_HOSTS`                       | List of hosts representing the host/domain names                                         | not set (required)                                           |
| `DJANGO_HOST_PROTOCOL`                       | Protocol host is running on (http or https)                                              | http                                                         |
| `DJANGO_HOST_DOMAIN`                         | Main host name server is reachable on                                                    | not set (required)                                           |
| `DJANGO_DATABASE_NAME`                       | Database name                                                                            | timed                                                        |
| `DJANGO_DATABASE_USER`                       | Database username                                                                        | timed                                                        |
| `DJANGO_DATABASE_HOST`                       | Database hostname                                                                        | localhost                                                    |
| `DJANGO_DATABASE_PORT`                       | Database port                                                                            | 5432                                                         |
| `DJANGO_OIDC_DEFAULT_BASE_URL`               | Base URL of the OIDC provider                                                            | http://timed.local/auth/realms/timed/protocol/openid-connect |
| `DJANGO_OIDC_OP_AUTHORIZATION_ENDPOINT`      | OIDC /auth endpoint                                                                      | {`DJANGO_OIDC_DEFAULT_BASE_URL`}/auth                        |
| `DJANGO_OIDC_OP_TOKEN_ENDPOINT`              | OIDC /token endpoint                                                                     | {`DJANGO_OIDC_DEFAULT_BASE_URL`}/token                       |
| `DJANGO_OIDC_OP_USER_ENDPOINT`               | OIDC /userinfo endpoint                                                                  | {`DJANGO_OIDC_DEFAULT_BASE_URL`}/userinfo                    |
| `DJANGO_OIDC_OP_JWKS_ENDPOINT`               | OIDC /certs endpoint                                                                     | {`DJANGO_OIDC_DEFAULT_BASE_URL`}/certs                       |
| `DJANGO_OIDC_RP_CLIENT_ID`                   | Client ID by your OIDC provider                                                          | timed-public                                                 |
| `DJANGO_OIDC_RP_CLIENT_SECRET`               | Client secret by your OIDC provider, should be None (flow start is handled by frontend)  | not set                                                      |
| `DJANGO_OIDC_RP_SIGN_ALGO`                   | Algorithm the OIDC provider uses to sign ID tokens                                       | RS256                                                        |
| `DJANGO_OIDC_VERIFY_SSL`                     | Verify SSL on OIDC request                                                               | dev: False, prod: True                                       |
| `DJANGO_OIDC_CREATE_USER`                    | Create new user if it doesn't exist in the database                                      | False                                                        |
| `DJANGO_OIDC_USERNAME_CLAIM`                 | Username token claim for user lookup / creation                                          | sub                                                          |
| `DJANGO_OIDC_EMAIL_CLAIM`                    | Email token claim for creating new users (if `DJANGO_OIDC_CREATE_USER` is enabled)       | email                                                        |
| `DJANGO_OIDC_FIRSTNAME_CLAIM`                | First name token claim for creating new users (if `DJANGO_OIDC_CREATE_USER` is enabled)  | given_name                                                   |
| `DJANGO_OIDC_LASTNAME_CLAIM`                 | Last name token claim for creating new users (if `DJANGO_OIDC_CREATE_USER` is enabled)   | family_name                                                  |
| `DJANGO_OIDC_BEARER_TOKEN_REVALIDATION_TIME` | Time (in seconds) to cache a bearer token before revalidation is needed                  | 60                                                           |
| `DJANGO_OIDC_CHECK_INTROSPECT`               | Use token introspection for confidential clients                                         | True                                                         |
| `DJANGO_OIDC_OP_INTROSPECT_ENDPOINT`         | OIDC token introspection endpoint (if `DJANGO_OIDC_CHECK_INTROSPECT` is enabled)         | {`DJANGO_OIDC_DEFAULT_BASE_URL`}/token/introspect            |
| `DJANGO_OIDC_RP_INTROSPECT_CLIENT_ID`        | OIDC client id (if `DJANGO_OIDC_CHECK_INTROSPECT` is enabled) of confidential client     | timed-confidential                                           |
| `DJANGO_OIDC_RP_INTROSPECT_CLIENT_SECRET`    | OIDC client secret (if `DJANGO_OIDC_CHECK_INTROSPECT` is enabled) of confidential client | not set                                                      |
| `DJANGO_OIDC_ADMIN_LOGIN_REDIRECT_URL`       | URL of the django-admin, to which the user is redirected after successful admin login    | dev: http://timed.local/admin/, prod: not set                |
| `DJANGO_ALLOW_LOCAL_LOGIN`                   | Enable / Disable login with local user/password (in admin)                               | True                                                         |
| `EMAIL_URL`                                  | Uri of email server                                                                      | smtp://localhost:25                                          |
| `DJANGO_DEFAULT_FROM_EMAIL`                  | Default email address to use for various responses                                       | webmaster@localhost                                          |
| `DJANGO_SERVER_EMAIL`                        | Email address error messages are sent from                                               | root@localhost                                               |
| `DJANGO_ADMINS`                              | List of people who get error notifications                                               | not set                                                      |
| `DJANGO_WORK_REPORT_PATH`                    | Path of custom work report template                                                      | not set                                                      |
| `UWSGI_INI`                                  | Path to uwsgi.ini configuration                                                          | /app/uwsgi.ini                                               |
| `UWSGI_MAX_REQUESTS`                         | uWSGI max requests                                                                       | 2000                                                         |
| `UWSGI_HARAKIRI`                             | uWSGI harakiri (request timeout)                                                         | 5                                                            |
| `UWSGI_PROCESSES`                            | uWSGI number of processes                                                                | 4                                                            |


## Contributing

Look at our [contributing guidelines](CONTRIBUTING.md) to start with your first contribution.

## License

Code released under the [GNU Affero General Public License v3.0](LICENSE).
