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
> This README-TH.md is presented in Thai. To read the English version of presentation, go to [README.md](https://github.com/ApisitPhysics/Apisit-Engine/blob/main/README.md)<br>
> README-TH.md นี้ ถูกนำเสนอในเวอร์ชันภาษาไทย หากต้องการอ่านการนำเสนอในเวอร์ชันภาษาอังกฤษให้ไปที่ [README.md](https://github.com/ApisitPhysics/Apisit-Engine/blob/main/README.md)

<div align="center">
  <h1>
    <i>บท</i> $ManimCe$
  </h1>
</div>

[ManimCe](https://www.manim.community) เป็นเครื่องมือที่ใช้สร้างแอนิเมชันทางคณิตศาสตร์ สามารถใช้ได้ด้วยการเขียนโปรแกรมภาษาไพทอน เป็นเวอร์ชันที่เหล่าคอมมูนิตี้ร่วมกันพัฒนาขึ้นต่อมาจาก Manim ต้นฉบับของ นายแกรนท์ แซนเดอร์ซัน และยังเป็นเจ้าของช่องยูทูป [3Blue1Brown](https://www.3blue1brown.com/) ช่องที่เผยแร่วิดีโอเกี่ยวกับคณิตศาสตร์เพื่อการศึกษา, สามารถดูตัวอย่างโค้ดของ ManimCe และ Manim3b1b ได้ตาม repository บน GitHub [ManimCommunity/manim](https://github.com/ManimCommunity/manim) และ [3b1b/manim](https://github.com/3b1b/manim) <br>

ManimCe อยู่ภายใต้ลิขสิทธิ์ MIT License 2 ฉบับได้แก่ ลิขสิทธิ๋โดย [3Blue1Brown LLC](https://github.com/ManimCommunity/manim/blob/main/LICENSE) และลิขสิทธิ์โดย [Manim Community Developers](https://github.com/ManimCommunity/manim/blob/main/LICENSE.community) โดยเนื้อหาใจความโดยสรุปของลิขสิทธิ์ทั้ง 2 ฉบับมีดังนี้

- Permissions (สิทธิที่ได้รับ)
  - Commercial use: ใช้ในเชิงพาณิชย์ได้
  - Modification: สามารถแก้ไขหรือดัดแปลงซอฟต์แวร์ได้
  - Distribution: สามารถแจกจ่ายหรือเผยแพร่ซอฟต์แวร์ได้
  - Private use: ใช้ส่วนตัวได้
- Limitations (ข้อจำกัด)
  - Liability: ไม่รับผิดชอบความเสียหายที่เกิดจากการใช้ซอฟต์แวร์
  - Warranty: ไม่มีการรับประกันใด ๆ เกี่ยวกับซอฟต์แวร์
- Conditions (เงื่อนไข)
  - License and copyright notice: ต้องระบุใบอนุญาตและประกาศลิขสิทธิ์เมื่อแจกจ่ายซอฟต์แวร์

บนข้อกำหนดดังกล่าว ผู้สร้างจะขอให้เครดิตกับ 3Blue1Brown และ ManimCe ด้วยการเพิ่มข้อความความที่บ่งบอกว่าเหล่าบุคคลเหล่านั้นเป็นผู้สร้างต้นฉบับของ Manim ใน [README-TH.md](https://github.com/ApisitPhysics/Apisit-Engine/blob/main/README-TH.md) [README.md](https://github.com/ApisitPhysics/Apisit-Engine/blob/main/README.md) [LICENSE](https://github.com/ApisitPhysics/Apisit-Engine/blob/main/LICENSE) และจะคงลิขสิทธิ์เดิมไว้ใน [LICENSE.3b1b](https://github.com/ApisitPhysics/Apisit-Engine/blob/main/LICENSE.3b1b) และ [LICENSE.community](https://github.com/ApisitPhysics/Apisit-Engine/blob/main/LICENSE.community)
<hr/>

<div align="center">
  <h1>
    <i>บท</i> $ManimAe$
  </h1>
</div>

ManimAe ย่อมาจาก Manim (Apisit's Edition) หมายถึง Manim ฉบับอภิสิทธิ์ เป็นเวอร์ชันที่พัฒนาต่อมาจากฟีเจอร์ที่มีอยู่แล้วใน ManimCe มีที่มาจาก เมื่ออภิสิทธิ์กำลังสร้างเครื่องมือสำหรับการทำแอนิเมชันให้ง่ายขึ้น แล้วจึงเอามาเผยแพร่เป็น ManimAe

ManimAe เป็นไลบรารีหนึ่งบนโปรแกรมภาษาไพทอน ซึ่งจะมีฟีเจอร์ต่างๆ รวมถึงผลลงานบางส่วนของอภิสิทธิ์จะถูกรวมไว้ในนี้ด้วย

สามารถติดตามผลงานของอภิสิทธิ์ได้ที่หน้าเฟสบุ๊คของเขา [อภิสิทธิ์ เส็งสูญ](https://www.facebook.com/share/1A1N9ye7y8)

> [!IMPORTANT]
> ManimAe นี้พัฒนาต่อมาจากต้นฉบับ ManimCe ดังนั้น เพื่อเป็นการให้เกียรติแก่ผู้สร้างต้นฉบับที่อนุญาตให้สามารถดัดแปลง และเผยแพร่ได้ตาม MIT license ทางผู้สร้าง ManimAe (อภิสิทธิ์ เส็งสูญ) จะอนุญาตให้บุคคลอื่นๆ สามารถนำ ManimAe ไปใช้ได้ตาม MIT License ด้วยเช่นกัน

## เนื้อหาในหน้านี้ :

- [ManimAe](#manimae)
- [บท ManimCe](#----บท-manimce--)
- [บท ManimAe](#----บท-manimae--)
  - [การติดตั้ง](#การติดตั้ง)
  - [การใช้งาน](#การใช้งาน)
  - [ช่องทางติดต่อ](#ช่องทางติดต่อ)
  - [ลิขสิทธิ์](#ลิขสิทธิ์)

## การติดตั้ง

> [!IMPORTANT]
> บนอุปกรณ์ของคุณต้องติดตั้งอุปกรณ์เหล่านี้ก่อน:<br>
> `Python` จาก https://www.python.org <br>
> `FFmpeg` จาก https://ffmpeg.org <br>
> `MiKTeX` จาก https:miktex.org <br>
> `ManimCe` จาก https://www.manim.community <br>
> `Git` จาก https://git-scm.com

หลังจากติดตั้งอุปกรณ์เหล่านี้แล้ว สำหรับระบบปฏิบัติการ `Windows` ให้กด `WIN+R` พิมพ์ `cmd` กด `ok` หรือ กด `WIN+S` พิมพ์ `cmd` เลือก `Command Promt` หรือวิธีการอื่นใดๆ ที่สามารถเปิด `Command Promt` ได้

หลังจากเปิด `Command Promt` แล้ว ให้คัดลอกคำสั่งด้านล่าง นำไปใส่ใน `Command Promt` กด `Enter` เพื่อติดตั้ง ManimAe

```plain tex
git clone https://github.com/ApisitPhysics/Apisit-Engine.git
cd Apisit-Engine/manimae
pip install .

```

เช็คว่า ManimAe ได้รับการติดตั้งแล้ว โดยพิมพ์คำสั่ง

```plain tex
pip show manimae

```

เท่านี้อุปกรณ์ของคุณก็ได้รับการติดตั้ง ManimAe เป็นที่เรียบร้อยแล้ว

> [!TIP]
> หากมีกระบวนการใด `error` แล้ว มีข้อแนะนำให้ตรวจสอบการติดตั้ง `Python` และ `Git` ว่าเป็นไปอย่างเรียบร้อยหรือไม่ แล้วลองติดตั้ง ManimAe อีกครั้ง

## การใช้งาน

> [!NOTE]
> ในเวอร์ชันกำลังพัฒนาซึ่งคือภายใน 1.x.x การใช้งานจะยังคงเป็นแบบ ManimCe อยู่ ในภายภาคหน้าจะมีการพัฒนาเพิ่มเติมอย่างแน่นอน

ในที่นี้หมายถึง การเรนเดอร์แอนิเมชัน ซึ่งสามารถอ่านวิธีการใช้ได้จาก [ManimCommunity/manim/README.md#usage](https://github.com/ManimCommunity/manim/blob/main/README.md#usage)

แต่จะขอกล่าววิธีการใช้งานเบื้องต้นไว้ดังนี้

```python
from manimae import * # เรียนใช้ไลบรารี manimae

class Example(Scene): # ถ่ายทอดคุณลักษณะจากคลาส Scene ซึ่งอยู่ใน ManimAe
  def construct(self):
    sq = Square()
    self.play(Write(sq))
    self.wait(2)

    text = Text("Text example")
    self.play(Transform(sq, text))
    self.wait(2)

```

วิธีการเรนเดอร์ไฟล์ ให้เปิด `cmd` ตามที่อยู่ของไฟล์นั้นๆ แล้วพิมพ์คำสั่ง

```plain text
manim file.py class -p
```

`manim` คือการเรียกใช้คำสั่ง `file.py` คือการเรียกใช้ไฟล์ภาษาไพทอนนั้นๆ `class` คลาสที่ต้องการเรนเดอร์ `-p` คำสั่งเพิ่มเติมในการเรนเดอร์

ยกตัวอย่างไฟล์ชื่อ Basic.py ให้เรนเดอร์คลาส Example

```plain tex
manim Basic.py Example -p
```

> หากมีกระบวนการใด `error` แล้ว มีข้อแนะนำให้ตรวจสอบการติดตั้ง `FFmepg`, `MiKTeX` และ `ManimCe` ว่าเป็นไปอย่างเรียบร้อยหรือไม่ แล้วลองติดตั้ง ManimAe อีกครั้ง

## ช่องทางติดต่อ

สามารถติดต่อ อภิสิทธิ์ เส็งสูญ ได้ที่
- เฟสบุ๊คของอภิสิทธิ์ [อภิสิทธิ์ เส็งสูญ](https://www.facebook.com/share/1A1N9ye7y8)
- อีเมลของอภิสิทธิ์ [ApisitPhysics@outlook.co.th](mailto:apisitphysics@outlook.co.th)
## ลิขสิทธิ์

ซอฟต์แวร์นี้อยู่ภายใต้ลิขสิทธิ์ MIT License โดย อภิสิทธิ์ เส็งสูญ [LICENSE](https://github.com/ApisitPhysics/Apisit-Engine/blob/main/LICENSE) และลิขสิทธิ์ต้นฉบับ 2 ฉบับ ได้แก่ 3Blue1Brown LLC [LICENSE.3b1b](https://github.com/ApisitPhysics/Apisit-Engine/blob/main/LICENSE.3b1b) และ Manim Community Developers [LICENSE.community](https://github.com/ApisitPhysics/Apisit-Engine/blob/main/LICENSE.community)
