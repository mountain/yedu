from PIL import Image, ImageDraw, ImageFont
import random

# ================= 配置区 =================
OUTPUT_FILE = "tree.png"

# 字体路径 (请确保路径正确)
FONT_PATH = "/Users/mingli/Library/Fonts/FZZhuYMXKJW.TTF"  # 方正祝允明小楷
SEAL_FONT_PATH = "/Users/mingli/Library/Fonts/FZZJ-MZFU.TTF"  # 方正字迹-穆钟复古印体 (或其他篆书字体)

# 1. 标题 (小楷册页通常标题较小，或者没有大标题，这里我们把它做得雅致一点)
TITLE_TEXT = "古诗"

# 2. 正文 (庭中有奇树)
TEXT_CONTENT = """
庭中有奇树
绿叶发华滋
攀条折其荣
将以遗所思
馨香盈怀袖
路远莫致之
此物何足贵
但感别经时
"""

# 3. 落款：修正为符合祝允明身份的落款
# 祝允明字希哲，号枝山，因右手有六指，自号"枝指生"。
SIGNATURE = """
乙巳仲冬
云境山房
允明书
"""

# 画布设置 (仿古宣纸色：偏黄一点)
CANVAS_WIDTH = 1800
CANVAS_HEIGHT = 1200  # 稍微加高一点，留出天地
BG_COLOR = (242, 236, 219)  # 仿古纸色
TEXT_COLOR_BASE = (30, 30, 30)  # 基础墨色 (不要纯黑)

# 字体参数调整 (小楷宜小，行距宜疏朗)
FONT_SIZE = 90  # 稍微调小，显得精致
TITLE_SIZE = 100
LINE_SPACING = 140  # 列与列的间距
CHAR_SPACING = 20  # 字与字的间距
START_X = CANVAS_WIDTH - 300  # 从右边开始
START_Y = 250


# ==========================================

def get_random_ink_color():
    """模拟墨色微小的干湿浓淡变化"""
    base = 30
    variation = random.randint(-10, 20)
    val = max(0, min(255, base + variation))
    return (val, val, val)


def create_calligraphy():
    image = Image.new("RGB", (CANVAS_WIDTH, CANVAS_HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
        title_font = ImageFont.truetype(FONT_PATH, TITLE_SIZE)
        sig_font = ImageFont.truetype(FONT_PATH, int(FONT_SIZE * 0.7))  # 落款字要小
        seal_font = ImageFont.truetype(SEAL_FONT_PATH, 50)
    except IOError as e:
        print(f"Error: 找不到字体文件. {e}")
        return

    current_x = START_X

    # ================= 1. 绘制标题 (更端庄) =================
    title_y = START_Y
    # 标题稍微靠上一点
    for char in TITLE_TEXT:
        # 小楷标题抖动要极小
        draw.text((current_x, title_y), char, font=title_font, fill=TEXT_COLOR_BASE)
        title_y += TITLE_SIZE + CHAR_SPACING + 10

    current_x -= int(LINE_SPACING * 1.8)  # 标题和正文隔开远一点

    # ================= 2. 绘制正文 (小楷矩阵感) =================
    lines = TEXT_CONTENT.strip().split('\n')

    for line in lines:
        current_y = START_Y + 30  # 正文比标题低一点，示谦卑
        for char in line:
            # 模拟手写微小误差，但保留魏晋法度的严谨
            offset_x = random.randint(-1, 1)
            offset_y = random.randint(-1, 1)

            # 使用动态墨色
            ink = get_random_ink_color()

            draw.text((current_x + offset_x, current_y + offset_y), char, font=font, fill=ink)
            current_y += FONT_SIZE + CHAR_SPACING

        current_x -= LINE_SPACING

    image.save(OUTPUT_FILE)
    print(f"✅ 已生成：{OUTPUT_FILE}")
    print("📝 备注：已修正印章为'祝允明印'，并优化了小楷的行列布局。")

if __name__ == "__main__":
    create_calligraphy()