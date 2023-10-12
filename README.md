# iCloudToolbox

## Overview

iCloudToolbox is a versatile tool designed for generating iCloud email addresses and importing them into a CSV file. This README provides an introduction to the project, explains its functionality, and highlights some important considerations.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Rate Limit and Maximum Email Limits](#rate-limit-and-maximum-email-limits)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Email Generation**: iCloudToolbox allows you to generate iCloud email addresses efficiently.
- **CSV Import**: Easily import the generated email addresses into a CSV file.
- **Cross-Platform**: Compatible with various operating systems.

## Installation

To install iCloudToolbox, follow these steps:

1. Clone this repository to your local machine.
   ```sh
   git clone https://github.com/your-username/icloudtoolbox.git
   ```
2. Navigate to the project directory.
   ```sh
   cd icloudtoolbox
   ```
3. Install the required dependencies.
   ```sh
   pip install -r requirements.txt
   ```

## Usage

After installation, you can run the program using the following command:

```sh
python icloudtoolbox.py
```

## Rate Limit and Maximum Email Limits

Please be aware of the following usage limitations:

- **Rate Limit**: After generating around 20 email addresses within an hour, the program may encounter rate limit issues imposed by iCloud. Avoid exceeding this limit to maintain smooth operation.

- **Maximum Emails for iCloud Accounts**: There seems to be a maximum limit of 600 email addresses that can be generated and imported into a specific iCloud account.

## Contributing

Contributions are welcome! If you'd like to enhance or fix issues with the program, please open a pull request. For major changes, discuss your ideas in the project's issue tracker.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
