import argparse
from norynix.core.runner import start_scan


def main():
    parser = argparse.ArgumentParser(prog="norynix")

    parser.add_argument(
        "-s",
        "--scan",
        metavar="TARGET",
        help="Target domain or IP"
    )

    args = parser.parse_args()

    if args.scan:
        start_scan(args.scan)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
