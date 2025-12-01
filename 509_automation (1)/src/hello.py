
import argparse

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(
        description="Greet user by name."
    )

    # Add a command-line argument
    parser.add_argument(
        "--name",
        required=True,          # must be provided
        help="Your name"        # shows in --help
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Use the parsed value
    print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()
