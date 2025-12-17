from PIL import Image, ImageDraw, ImageFont
import random

# ================= 配置区 =================
# 输出文件名
OUTPUT_FILE = "plum.png"

# 字体路径
FONT_PATH = "/Users/mingli/Library/Fonts/FZWangDXCJF.TTF"
SEAL_FONT_PATH = "/Users/mingli/Library/Fonts/FZZJ-MZFU.TTF"

# 1. 标题
TITLE_TEXT = "墨梅"

# 2. 正文
TEXT_CONTENT = """
我家洗硯池頭樹
個個花開淡墨痕
不要人誇好顏色
只留清氣滿乾坤
"""

# 3. 修改后的落款：乙巳(2025) + 仲冬 + 灵境山房
SIGNATURE = "乙巳仲冬"

# 画布设置
CANVAS_WIDTH = 2400
CANVAS_HEIGHT = 1400
BG_COLOR = (245, 240, 225)
TEXT_COLOR = (20, 20, 20)

FONT_SIZE = 110
LINE_SPACING = 160
CHAR_SPACING = 15
START_X = CANVAS_WIDTH - 250
START_Y = 200


# ==========================================

def create_calligraphy():
    image = Image.new("RGB", (CANVAS_WIDTH, CANVAS_HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
        title_font = ImageFont.truetype(FONT_PATH, int(FONT_SIZE * 1.2))
        small_font = ImageFont.truetype(FONT_PATH, int(FONT_SIZE * 0.6))
        seal_font = ImageFont.truetype(SEAL_FONT_PATH, 50)
    except IOError:
        print(f"Error: 找不到字体文件 {FONT_PATH}")
        return

    current_x = START_X
    current_y = START_Y

    # ================= 绘制标题 =================
    title_start_y = START_Y + 50
    for char in TITLE_TEXT:
        offset_x = random.randint(-1, 1)
        offset_y = random.randint(-1, 1)
        draw.text((current_x + offset_x, title_start_y + offset_y), char, font=title_font, fill=TEXT_COLOR)
        title_start_y += int(FONT_SIZE * 1.2) + CHAR_SPACING

    current_x -= int(LINE_SPACING * 1.5)

    # ================= 绘制正文 =================
    clean_content = TEXT_CONTENT.strip().split('\n')
    for line in clean_content:
        current_y = START_Y + random.randint(-30, 30)
        for char in line:
            offset_x = random.randint(-2, 2)
            offset_y = random.randint(-2, 2)
            draw.text((current_x + offset_x, current_y + offset_y), char, font=font, fill=TEXT_COLOR)
            current_y += FONT_SIZE + CHAR_SPACING
        current_x -= LINE_SPACING

    image.save(OUTPUT_FILE)
    print(f"成功生成赛博版书法：{OUTPUT_FILE}")


if __name__ == "__main__":
    create_calligraphy()