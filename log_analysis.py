a = input("Enter the log file name: ")
b = input("Enter the file name in which you want to save output: ")


def log_analyze():
    counts = {
        "INFO": 0,
        "ERROR": 0,
        "WARNING": 0
    }

    try:
        with open(a, "r") as f:
            lines = f.readlines()

        if not lines:
            print("The log file is empty")
            return

        for data in lines:
            for level in counts:
                if level in data:
                    counts[level] += 1

        summary = (
            f"Log Summary\n"
            f"-----------\n"
            f"INFO: {counts['INFO']}\n"
            f"WARNING: {counts['WARNING']}\n"
            f"ERROR: {counts['ERROR']}\n"
        )

        print(summary)

        with open(b, "w") as file:
            file.write(summary)

        print(f"Summary written to {b}")

    except FileNotFoundError:
        print(f"Error: '{a}' not found.")

    except Exception as error:
        print(f"Unexpected error: {error}")


log_analyze()
