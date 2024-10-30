# PO File Merger Tool

A lightweight desktop app for merging `.po` translation files across culture-specific folders, streamlining localization workflows for Unreal Engine and other multi-language projects.

![image](https://github.com/user-attachments/assets/ff68e759-76cf-4015-a171-3a022dca5992)


### Usage
1. **Select Folder**: Click the "Select Folder" button to choose the root localization folder containing culture folders (e.g., en-US, fr-FR).

2. **Start Merging**: After selecting, the app will automatically merge .po files inside each culture folder.

3. **Track Progress**: The progress bar and status label display the merging status for each folder.

4. **Completion**: Once finished, a pop-up will confirm that all .po files have been merged successfully.

Each culture folder will now contain a merged.po file with consolidated translations by default. However, if you select the Custom Output Path option, all merged .po files will be saved in a single output folder, with each file prefixed by its culture code (e.g., en-US_merged.po, fr-FR_merged.po).

## Installation

### Prerequisites
- **Python 3.6+**: Required to build or modify the app.
- **polib**: A Python library for working with `.po` files. Install via pip:
  ```bash
  pip install polib

  ### Using the Executable
1. Download the latest release from the [Releases page](link-to-releases).
2. Run the `.exe` file (no additional setup required).

### Building from Source
If you prefer to build from source:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/po-file-merger.git
   cd po-file-merger

2. Run the app:
   ```bash
   python po_merger_app.py

4. To compile into an executable, install PyInstaller and run:
   ```bash
   pyinstaller --onefile --windowed po_merger_app.py

