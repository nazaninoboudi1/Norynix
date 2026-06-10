from norynix.config.settings import CONFIG
from norynix.modules.tech_detect import detect_technologies
from norynix.modules.js_recon import extract_js_files

import asyncio
import httpx
import re


async def probe_host(client, host):

    results = []

    for scheme in CONFIG["schemes"]:

        url = f"{scheme}://{host}"

        try:
            response = await client.get(
                url,
                follow_redirects=CONFIG.get("follow_redirects", True)
            )

            title = "N/A"

            match = re.search(
                r"<title>(.*?)</title>",
                response.text,
                re.IGNORECASE | re.DOTALL
            )

            if match:
                title = match.group(1).strip()

            technologies = detect_technologies(
                response.headers,
                response.text
            ) or []

            js_files = extract_js_files(response.text) or []

            js_files = [j for j in js_files if j and j.strip()]

            results.append({
                "url": url,
                "status": response.status_code,
                "title": title,
                "technologies": technologies,
                "js_files": js_files
            })

        except Exception:
            continue

    return results


async def probe_many(hosts):

    limits = httpx.Limits(
        max_connections=100,
        max_keepalive_connections=20
    )

    timeout = httpx.Timeout(CONFIG.get("timeout", 5.0))

    async with httpx.AsyncClient(
        timeout=timeout,
        limits=limits
    ) as client:

        tasks = [probe_host(client, host) for host in hosts]

        return await asyncio.gather(*tasks)