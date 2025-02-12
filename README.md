<div align="center">
  <h1>$ManimAe$</h1>
  <p>
    $$
    \begin{align*}
    Manim \; (Apisit's \; Edition) \; &| \; Manim \; (ฉบับอภิสิทธิ์) \\
    \text{Further developed from the original} \; ManimCe \; &| \; \text{พัฒนาเพิ่มเติมจากต้นฉบับ} \; ManimCe \\
    \text{Scine 8/02/2025} \; &| \; \text{ตั้งแต่ 8/ก.พ./2568}
    \end{align*}
    $$
  </p>
</div>
<hr/>

> [!NOTE]
> This README.md is presented in English. To read the Thai version of presentation, go to [README-TH.md](https://github.com/ApisitPhysics/Apisit-Engine/blob/main/README-TH.md)<br>
> README.md นี้ ถูกนำเสนอในเวอร์ชันภาษาอังกฤษ หากต้องการอ่านการนำเสนอในเวอร์ชันภาษาไทยให้ไปที่ [README-TH.md](https://github.com/ApisitPhysics/Apisit-Engine/blob/main/README-TH.md)

<div align="center">
  <h1>
    <i>Chapter</i> $ManimCe$
  </h1>
</div>

[ManimCe](https://www.manim.community) is an animation engine for explanatory math videos and works with Python programming. It is a community-developed version based on the original work by Grant Sanderson, the creator of the YouTube channal [3Blue1Brown](https://www.3blue1brown.com/), which publishes about educational math videos. You can check out example code for both ManimCE and Manim3b1b on GitHub at [ManimCommunity/manim](https://github.com/ManimCommunity/manim) and [3b1b/manim](https://github.com/3b1b/manim) <br>

ManimCe is double-licensed under the MIT license, with copyright by [3Blue1Brown LLC](https://github.com/ManimCommunity/manim/blob/main/LICENSE) and copyright by [Manim Community Developers](https://github.com/ManimCommunity/manim/blob/main/LICENSE.community). These conditions apply to its usage..

- Permissions
  - Commercial use
  - Modification
  - Distribution
  - Private use
- Limitations
  - Liability:
  - Warranty
- Conditions
  - License and copyright notice

Under these conditions, the creator must give credit to 3Blue1Brown and ManimCE by adding text acknowledging them as the original creators of Manim. This credit should be included in [README-TH.md](https://github.com/ApisitPhysics/Apisit-Engine/blob/main/README-TH.md),  [README.md](https://github.com/ApisitPhysics/Apisit-Engine/blob/main/README.md) and [LICENSE](https://github.com/ApisitPhysics/Apisit-Engine/blob/main/LICENSE), while the original licenses should be retained in [LICENSE.3b1b](https://github.com/ApisitPhysics/Apisit-Engine/blob/main/LICENSE.3b1b) and [LICENSE.community](https://github.com/ApisitPhysics/Apisit-Engine/blob/main/LICENSE.community)
<hr/>

<div align="center">
  <h1>
    <i>Chapter</i> $ManimAe$
  </h1>
</div>

ManimAe stands for Manim (Apisit's Edition), meaning "Apisit's version of Manim." It is a version developed further from the existing features in ManimCe. The idea originated when Apisit was creating tools to simplify animation production, which were then released as ManimAe.

ManimAe is a library in the Python programming language, which includes various features, along with some of Apisit's work that has been incorporated into it.

You can follow Apisit's work on his Facebook page. [Apisit Sengsoon](https://www.facebook.com/share/1A1N9ye7y8)

> [!IMPORTANT]
> ManimAe is developed as an extension of the original ManimCE. Therefore, to honor the original creators who allowed modifications and distribution under the MIT License, the creator of ManimAe (Apisit Sengsoon) will also allow others to use ManimAe under the same MIT License.

## On this page:

- [ManimAe](#manimae)
- [Chapter ManimCe](#----chapter-manimce--)
- [Chapter ManimAe](#----chapter-manimae--)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contact](#contact)
  - [License](#license)

## Installation

> [!IMPORTANT]
> These dependencies must be installed on your device first.:<br>
> `Python` from https://www.python.org <br>
> `FFmpeg` from https://ffmpeg.org <br>
> `MiKTeX` from https://miktex.org <br>
> `ManimCe` from https://www.manim.community <br>
> `Git` from https://git-scm.com

After installing these dependencies, for the Windows operating system, press `WIN+R`, type `cmd`, and click `OK`, or press `WIN+S`, type `cmd`, select `Command Prompt`, or use any other method to open `Command Prompt`.

Once `Command Prompt` is open, copy the command below, paste it into `Command Prompt`, and press `Enter` to install ManimAe.

```plain tex
git clone https://github.com/ApisitPhysics/Apisit-Engine.git
cd Apisit-Engine/manimae
pip install .

```

To check if ManimAe has been installed successfully, type the following command.

```plain tex
pip show manimae

```

That's it. Your device has successfully installed ManimAe.

> [!TIP]
> If any process results in an `error`, it is recommended to check whether `Python` and `Git` are installed correctly. If not, please ensure they are properly installed and then try installing ManimAe again.

## Usage

> [!NOTE]
> In the developing version, which is within 1.x.x, the usage will still follow the structure of ManimCE. However, future updates will definitely include additional developments.

his refers to rendering animations, and you can read the usage instructions in [ManimCommunity/manim/README.md#usage](https://github.com/ManimCommunity/manim/blob/main/README.md#usage)

However, here is a brief guide on how to use it.

```python
from manimae import * # use the manimae library

class Example(Scene): # inherit properties from the Scene class, which is part of ManimCe.
  def construct(self):
    sq = Square()
    self.play(Write(sq))
    self.wait(2)

    text = Text("Text example")
    self.play(Transform(sq, text))
    self.wait(2)

```

To render the file, navigate to the directory of the file using cmd and then type the following command.

```plain text
manim file.py class -p
```

`manim` is the command to run Manim. `file.py` is the Python file you're working with. `class` is the specific scene or class you want to render from that file. `-p` is an additional flag to automatically play the rendered video once it's done.

For example, to render the `Example` class from a file named `Basic.py`, you would use the following command.

```plain tex
manim Basic.py Example -p
```

> [!TIP]
> If any process results in an `error`, it is recommended to check whether `FFmpeg`, `MiKTeX` and `ManimCe` are installed correctly. If not, please ensure they are properly installed and then try installing ManimAe again.

## Contact

You can contact Apisit Sengsoon at, 
- Facebook [Apisit Sengsoon](https://www.facebook.com/share/1A1N9ye7y8)
- Email [ApisitPhysics@outlook.co.th](mailto:apisitphysics@outlook.co.th)

## License

This software is licensed under the MIT License by Apisit Sengsoon [LICENSE](https://github.com/ApisitPhysics/Apisit-Engine/blob/main/LICENSE) and includes the original copyrights from two sources 3Blue1Brown LLC [LICENSE.3b1b](https://github.com/ApisitPhysics/Apisit-Engine/blob/main/LICENSE.3b1b) and Manim Community Developers [LICENSE.community](https://github.com/ApisitPhysics/Apisit-Engine/blob/main/LICENSE.community)
