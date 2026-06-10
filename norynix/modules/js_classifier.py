def classify_js(js_url: str):

    if not js_url:
        return "unknown"

    js_url = js_url.lower()

    if "googleapis.com" in js_url:
        return "api"

    if js_url.startswith("http"):
        return "cdn"

    return "internal"
