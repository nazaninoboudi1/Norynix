import dns.resolver

def enumerate_dns(target):
    results = {}

    for record_type in ["A", "AAAA", "MX", "NS"]:
        try:
            answers = dns.resolver.resolve(target, record_type)

            results[record_type] = [
                str(answer)
                for answer in answers
            ]

        except Exception:
            results[record_type] = []

    return results
