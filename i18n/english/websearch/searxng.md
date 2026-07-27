---
description: Deploy a SearXNG instance for Cherry Studio V2 and configure JSON, search engines, and basic authentication.
icon: searchengin
---

# Deploy and Configure SearXNG Locally

SearXNG is an open-source metasearch engine that aggregates results from multiple search engines in your own instance. Cherry Studio V2 can use a self-hosted SearXNG instance as its keyword search provider. This option suits users who value control and privacy and have basic container administration skills.

{% hint style="info" %}
SearXNG itself is open source, but running an instance still uses local or server resources. Its upstream search engines may also impose their own access restrictions. Self-hosting does not automatically guarantee search quality, availability, or anonymity.
{% endhint %}

## Before Choosing SearXNG

Unlike a search service where you enter an API Key directly, SearXNG requires an accessible instance first.

| Deployment | Best for | Considerations |
| --- | --- | --- |
| Local | Personal use and quick testing | Only the local computer can access it directly; the service stops when the computer is shut down |
| LAN | Sharing among multiple trusted devices | Requires correct listening-address and firewall configuration |
| Public self-hosting | Cross-network or team use | Requires HTTPS, authentication, rate limiting, updates, and logging considerations |
| Public instance | Temporary testing | May disable the JSON API, impose rate limits, or become unavailable at any time |

Do not use an unfamiliar public instance as a long-term default provider. The instance administrator may see query and connection information, and public instances generally provide no availability guarantee.

## Cherry Studio Instance Requirements

A usable SearXNG instance must meet these requirements:

- The device running Cherry Studio can access the instance address;
- `/config` returns the instance configuration;
- `/search` allows `format=json`;
- At least one enabled search engine belongs to both the `general` and `web` categories;
- Web pages in search results are accessible from the network where Cherry Studio runs;
- If the reverse proxy enables HTTP Basic Auth, the same credentials are entered in Cherry Studio.

Cherry Studio uses this address by default:

```text
http://localhost:8080
```

This is only a preset. The actual port and domain must match your deployment.

## Deploy with the Official Container Template

SearXNG officially recommends a Docker or Podman Compose template. The following steps are for users who already have Docker and Docker Compose installed. A production environment also requires your own backup, update, and access-control plan.

### 1. Prepare the Directory and Template

```bash
mkdir -p ./searxng/core-config
cd ./searxng
curl -fsSLO https://raw.githubusercontent.com/searxng/searxng/master/container/docker-compose.yml
curl -fsSLO https://raw.githubusercontent.com/searxng/searxng/master/container/.env.example
cp .env.example .env
```

Open `.env` and follow the template instructions to check the port, instance address, secrets, and other settings. The template may change as SearXNG is updated. Before an initial deployment or upgrade, read the [official container installation documentation](https://docs.searxng.org/admin/installation-docker.html).

### 2. Enable JSON Output

Add at least the following to `core-config/settings.yml`:

```yaml
use_default_settings: true

search:
  formats:
    - html
    - json
```

{% hint style="warning" %}
Cherry Studio requests `format=json`. If `search.formats` in SearXNG does not include `json`, the search endpoint usually returns `403 Forbidden`.
{% endhint %}

If you already have a `settings.yml`, merge the `json` item into it. Do not overwrite your existing engine, proxy, language, or security configuration with the minimal example above.

### 3. Start the Instance

```bash
docker compose up -d
docker compose ps
```

To view logs:

```bash
docker compose logs -f core
```

Service names may change with the official template. If the log command cannot find `core`, run `docker compose ps` first and use the actual service name.

### 4. Verify the Instance

Open the instance home page in a browser, then verify the JSON API in a terminal. Assuming the address is `http://127.0.0.1:8080`:

```bash
curl "http://127.0.0.1:8080/config"
curl "http://127.0.0.1:8080/search?q=Cherry+Studio&format=json"
```

Both requests should return JSON. The second response should also contain usable search results.

For SearXNG endpoint and parameter details, see the [Search API](https://docs.searxng.org/dev/search_api.html).

## Configure SearXNG in Cherry Studio

### 1. Open SearXNG Settings

Open:

> **Settings → Web Search → SearXNG**

### 2. Enter the API Host

Enter the instance root address. Do not manually append `/search` or `/config`.

Local example:

```text
http://127.0.0.1:8080
```

Public example:

```text
https://search.example.com
```

Cherry Studio appends `/config` and `/search` automatically.

{% hint style="info" %}
The Cherry Studio desktop app runs directly on the host system. When Docker maps the port to the host, normally use `127.0.0.1:mapped-port`; you do not need `host.docker.internal`.
{% endhint %}

### 3. Enter Basic Authentication

If the reverse proxy is configured with HTTP Basic Auth:

1. Enter the username in SearXNG settings;
2. Enter the corresponding password;
3. Do not put `username:password` in the API Host.

Whenever the username is nonempty, Cherry Studio sends a Basic Auth request header with `/config`, `/search`, and check requests.

For a public connection, HTTP Basic Auth must be used with HTTPS. Using Basic Auth without HTTPS may expose credentials in transit.

### 4. Check the Connection

Click **Check**.

After the check succeeds, set SearXNG as the default keyword search provider. You can then use it by enabling the Globe icon in a conversation.

## How Cherry Studio Selects Search Engines

If no separate engine list has been saved, Cherry Studio reads:

```text
GET /config
```

It selects engines that meet all of these conditions:

- `enabled` is `true`;
- `categories` contains `general`;
- `categories` contains `web`.

The app then makes a request similar to:

```text
GET /search?q=query&language=auto&format=json&engines=engine-list
```

Changing a one-time search preference in the SearXNG web interface therefore does not necessarily change Cherry Studio's request. Enable appropriate engines and categories persistently in the instance's `settings.yml`.

### Keep Only Specific Engines

If some upstream engines are inaccessible from your current network, adjust the engines in `settings.yml`. Example:

```yaml
use_default_settings:
  engines:
    keep_only:
      - duckduckgo
      - wikipedia
```

Engine names, availability, and settings may change with SearXNG updates. Confirm exact names in the instance's `/config` response or preferences first, and see the [engine configuration documentation](https://docs.searxng.org/admin/settings/settings_engines.html).

{% hint style="warning" %}
Do not copy a fixed engine list that does not suit your network. Search engines may restrict access by region, trigger CAPTCHAs, or change their interfaces. Use instance logs and actual searches as the final reference.
{% endhint %}

## Search Results and Web Page Retrieval

After SearXNG returns titles, summaries, and URLs, Cherry Studio attempts to retrieve the main text from the result pages and keeps only content that was retrieved successfully.

This means:

- The maximum result count limits how many candidate URLs the app processes;
- Retrieval may fail for pages that require sign-in, block automated access, or are inaccessible from the current network;
- If every candidate page fails to load, the search may return an error or have no usable results;
- SearXNG remains a keyword search provider. The default URL retrieval provider used when a URL is pasted directly must still be selected separately in Web Search settings.

## Security Recommendations for Public Deployment

Do not expose an unprotected SearXNG administration or search endpoint directly to the public internet.

At minimum, consider:

- Enabling HTTPS with a trusted certificate;
- Configuring access authentication at the reverse-proxy layer;
- Keeping reasonable rate limits and bot protection;
- Restricting administration ports and unnecessary network entry points;
- Regularly updating SearXNG, container images, and the reverse proxy;
- Avoiding long-term storage of sensitive queries in access logs;
- Providing credentials only to trusted users and rotating them regularly.

Cherry Studio currently supports HTTP Basic Auth, but it does not configure server-side TLS, permissions, or rate limits for you.

## Troubleshooting

### Check Returns 403

The most common cause is that JSON output is disabled. Confirm that `settings.yml` includes:

```yaml
search:
  formats:
    - html
    - json
```

Save the file, restart the instance, and verify it by directly opening `/search?q=test&format=json`.

A public instance may also disable the JSON API intentionally. In that case, switch instances or deploy your own.

### Check Returns 401

The instance or reverse proxy requires authentication:

- Enter the correct Basic Auth username and password in Cherry Studio;
- Confirm that the reverse proxy uses the same credentials to protect `/config` and `/search`;
- Check whether the username or password includes spaces copied by mistake;
- Do not append credentials to the URL.

### No Usable general/web Engine

Cherry Studio could not find an enabled engine in `/config` that belongs to both `general` and `web`.

Check:

1. Whether `/config` returns `engines` correctly;
2. Whether the target engine has `enabled: true`;
3. Whether `categories` contains both `general` and `web`;
4. Whether the instance was restarted or reloaded after the configuration change.

### Searches Time Out or Results Are Unstable

Review the SearXNG logs and check:

- Whether an upstream search engine returns 403, 429, or a CAPTCHA;
- Whether DNS, the proxy, and the server's outbound network work correctly;
- Whether the instance request timeout is too short;
- Whether the selected engines are suitable for the current region;
- Whether the device running Cherry Studio can open the result web pages.

Do not simply disable all rate limits and security protections. Determine whether the restriction occurs in SearXNG, the reverse proxy, an upstream engine, or the local network.

### Search Works in a Browser, but Cherry Studio Still Fails

The browser page uses HTML by default, while Cherry Studio requires JSON. Test both:

```text
/config
/search?q=test&format=json
```

Also confirm that API Host contains only the root address, Basic Auth is correct, and the reverse proxy does not block these two paths separately.

### Results Are Returned, but the Answer Has No Citations

The result page text may have failed to load, or the model may not have used the search results correctly. You can:

- Remove search engines that are inaccessible or require sign-in;
- Increase the maximum result count and try again;
- Switch to engines better suited to the current network;
- Explicitly ask for sources in the question;
- Confirm that the model supports tool calling.

## Updates and Maintenance

Before updating the service, read the SearXNG migration notes and back up `.env` and `core-config`. With a container deployment, you will usually need to update the official template and pull a new image; do not assume an old Compose file will remain compatible forever.

Official resources:

- [SearXNG Container Installation](https://docs.searxng.org/admin/installation-docker.html)
- [SearXNG `settings.yml`](https://docs.searxng.org/admin/settings/settings.html)
- [Search Output Formats](https://docs.searxng.org/admin/settings/settings_search.html)
- [Administration API `/config`](https://docs.searxng.org/admin/api.html)
- [SearXNG GitHub](https://github.com/searxng/searxng)

## Related Documentation

- [Web Search](README.md)
- [Free Web Search](mian-fei-lian-wang-mo-shi.md)
- [Web Search Blacklist](blacklist.md)

***

### Get Help and Submit Feedback

If you encounter a problem during setup or use, submit feedback through the official channels listed in [Feedback and Suggestions](../question-contact/suggestions.md). Include the Cherry Studio version, SearXNG version, error code, and sanitized logs, but do not submit real domain credentials or authentication passwords.
