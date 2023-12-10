
# WhatsApp Secret Santa

## Introduction

`secret-santa` is a Python application designed to simplify organizing Secret Santa events. It randomly assigns participants to each other while ensuring no one gets paired with their significant other. The app also facilitates sending customized messages via WhatsApp.

## Dependencies

- Python
- Poetry (for package management)
- Selenium (for web automation)

## Installation and Setup

1. **Install Poetry**: Follow the installation instructions for Poetry from [here](https://python-poetry.org/docs/).

2. **Clone the Repository**:

    ```bash
    git clone https://github.com/your-repo/secret-santa.git
    cd secret-santa
    ```

3. **Install Dependencies**:

    ```bash
    poetry install
    ```

4. **Activate the Poetry Shell**:

    ```bash
    poetry shell
    ```

5. **Setup Participants**:

    - Copy `data.py.example` to `data.py`.
    - Edit `data.py` with participant details, including couples and phone numbers.
6. **Customize Messages** (Optional):

    - Modify `generated_text` in `main.py` to customize the messages sent via WhatsApp.

## Running the Script

1. **Navigate to the Script Directory**:

    ```bash
    cd secret-santa/secret-santa/
    ```

2. **Run the Script**:

    ```bash
    python main.py
    ```

3. **WhatsApp Setup**:

    - A browser window will open.
    - Scan the WhatsApp QR code with your phone.
    - Ensure all participant phone numbers are saved in your contacts.

4. **Complete the Process**:

    - Wait for the script to send messages.
    - Once done, close the browser.

## Notes

- Ensure your device remains connected to the internet during the process.
- Review and test the script in a controlled environment before actual use.
