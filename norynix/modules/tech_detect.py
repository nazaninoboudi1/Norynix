def detect_technologies(headers, html):

    tech = []

    headers_l = {
        k.lower(): v.lower()
        for k, v in headers.items()
    }

    server = headers_l.get("server", "")
    powered = headers_l.get("x-powered-by", "")

    # Server-based detection
    if "nginx" in server:
        tech.append("Nginx")

    if "apache" in server:
        tech.append("Apache")

    if "cloudflare" in server:
        tech.append("Cloudflare")

    # Backend detection
    if "php" in powered:
        tech.append("PHP")

    if "asp.net" in powered:
        tech.append("ASP.NET")

    if "express" in server:
        tech.append("Node.js")

    # HTML patterns (important upgrade)
    html_lower = html.lower()

    if "wp-content" in html_lower or "wp-includes" in html_lower:
        tech.append("WordPress")

    if "react" in html_lower:
        tech.append("React")

    if "__next" in html_lower:
        tech.append("Next.js")

    return list(set(tech))