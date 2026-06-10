import re


def extract_js_files(html):

    if not html:
        return []

    raw = re.findall(
        r'<script[^>]+src=["\'](.*?)["\']',
        html,
        re.IGNORECASE
    )

    clean = set()

    for js in raw:

        if not js:
            continue

        js = js.strip()

        # ❌ حذف empty و whitespace-only
        if js == "":
            continue

        if len(js) == 0:
            continue

        # ❌ حذف invalid
        if js.isspace():
            continue

        # ❌ حذف data URI
        if js.startswith("data:"):
            continue

        clean.add(js)

    return list(clean)