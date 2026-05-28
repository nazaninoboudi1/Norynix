from norynix.config.settings import CONFIG

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
                follow_redirects=CONFIG[
                    "follow_redirects"
                ]
            )

            title = "N/A"

            match = re.search(
                r"<title>(.*?)</title>",
                response.text,
                re.IGNORECASE | re.DOTALL
            )

            if match:
                title = match.group(1).strip()

            results.append({
                "url": url,
                "status": response.status_code,
                "title": title
            })

        except Exception:
            pass

    return results


async def probe_many(hosts):

    limits = httpx.Limits(
        max_connections=100,
        max_keepalive_connections=20
    )

    async with httpx.AsyncClient(

        timeout=CONFIG["timeout"],

        limits=limits

    ) as client:

        tasks = [
            probe_host(client, host)
            for host in hosts
        ]

        return await asyncio.gather(
            *tasks
        )