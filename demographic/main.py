# This entrypoint file to be used in development. Start by reading README.md
import demo
from unittest import main

# Test your function by calling it here
demo.calculate_demographic_data()

# Run unit tests automatically
main(module='test_module', exit=False)